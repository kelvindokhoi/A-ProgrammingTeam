# Star Wars Movies
# https://open.kattis.com/problems/starwarsmovies

# python Star_Wars_Movies.py < Star_Wars_Movies_in.txt
# from typing import Union
import traceback

Q_num_queries = int(input())

class Node:
    def __init__(self,movie_index,plot_index) -> None:
        self.movie_index = movie_index
        self.plot_index = plot_index
        self.offset = 0
        self.left = None
        self.right = None
    def set_left(self,node) -> None:
        self.left = node
    def set_right(self,node) -> None:
        self.right = node
    def get_left(self):
        return self.left
    def get_right(self):
        return self.right

class MovieTree:
    def __init__(self) -> None:
        self.root = None
        self.movie_index = 1
    
    def get_movie_index(self) -> int:
        self.movie_index += 1
        return self.movie_index-1

    def findNode(self,plot_index) -> tuple[Node | None, Node | None, int]:
        if self.root is None:
            return None, None, 0
        prev = None
        curr = self.root
        offset = 0
        while True:
            if curr is None:
                print("Not found")
                return curr, prev, offset
            if curr.plot_index + offset==plot_index:
                return curr, prev, offset
            else:
                if curr.plot_index + offset > plot_index:
                    offset += curr.offset
                    prev = curr
                    curr = curr.get_left()
                elif curr.plot_index + offset + curr.offset < plot_index:
                    offset += curr.offset
                    prev = curr
                    curr = curr.get_right()

    def addNode(self,plot_index):
        newNode = Node(self.get_movie_index(),plot_index)
        if self.root is None:
            self.root = newNode
            return
        curr, prev, offset = self.findNode(plot_index)

        if prev is None:
            if curr.offset + offset < plot_index:
                newNode.set_right(curr)
            else:
                newNode.set_left(curr)
            return
        if prev.offset + offset == plot_index:
            newNode.set_right(curr)
            prev.set_right(newNode)
            newNode.offset += 1
            return
        elif prev.offset + offset < plot_index:
            if prev.get_right() is None:
                prev.set_right(newNode)
            else:
                if curr.offset + offset < plot_index:
                    newNode.set_right(curr)
                else:
                    newNode.set_left(curr)
                prev.set_right(newNode)
        else:
            if prev.get_left() is None:
                prev.set_left(newNode)
            else:
                if curr.offset + offset < plot_index:
                    newNode.set_right(curr)
                else:
                    newNode.set_left(curr)
                prev.set_left(newNode)
    
    def returnMovieIndex(self,plot_index):
        curr, prev, offset = self.findNode(plot_index)
        if curr is not None:
            return curr.movie_index + offset

MVT = MovieTree()
for _ in range(Q_num_queries):
    command, par = map(int,input().split())
    print("Executing...")
    try:
        if command==1:
            MVT.addNode(par)
        else:
            print(MVT.returnMovieIndex(par))
    except Exception:
        print(f"Failed at {command} {par}")
        print(traceback.format_exc())
        exit()
        
    