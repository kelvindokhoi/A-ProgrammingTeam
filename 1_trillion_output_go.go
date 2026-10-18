package main
import (
    "bufio"
    "os"
    "time"
)

func main() {
    t0 := time.Now()
    writer := bufio.NewWriterSize(os.Stdout, 4*1024)
    for i:=0;i<1_000_000_000_000;i++{
        
    }
    t1 := time.Now()
    elapsed := t1.Sub(t0)
    writer.Write([]byte("Time taken in total: " + elapsed.String() + "\n"))
    writer.Flush()
}