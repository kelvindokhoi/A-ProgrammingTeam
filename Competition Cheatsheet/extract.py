import zipfile
import xml.etree.ElementTree as ET
import sys
import os

def extract_text_from_docx(docx_path, out_path):
    namespaces = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
    if not os.path.exists(docx_path):
        print(f"File not found: {docx_path}")
        return
        
    try:
        with open(out_path, 'w', encoding='utf-8') as f:
            with zipfile.ZipFile(docx_path, 'r') as docx:
                xml_content = docx.read('word/document.xml')
                tree = ET.fromstring(xml_content)
                
                for paragraph in tree.findall('.//w:p', namespaces):
                    texts = []
                    for node in paragraph.iter():
                        if node.tag == f"{{{namespaces['w']}}}t" and node.text:
                            texts.append(node.text)
                        elif node.tag == f"{{{namespaces['w']}}}br":
                            texts.append('\n')
                    text = "".join(texts)
                    if text:
                        f.write(text + '\n')
        print(f"Successfully extracted to {out_path}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    extract_text_from_docx(sys.argv[1], sys.argv[2])
