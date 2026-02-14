import fitz  # PyMuPDF
from typing import Dict, List
import base64
from io import BytesIO
from PIL import Image

class PDFParser:
    """Extract text and images from PDF files"""
    
    @staticmethod
    def extract_text(pdf_path: str) -> str:
        """Extract all text from PDF"""
        doc = fitz.open(pdf_path)
        text = ""
        for page in doc:
            text += page.get_text()
        doc.close()
        return text
    
    @staticmethod
    def extract_text_by_page(pdf_path: str) -> List[Dict]:
        """Extract text page by page"""
        doc = fitz.open(pdf_path)
        pages = []
        for page_num, page in enumerate(doc):
            pages.append({
                "page_number": page_num + 1,
                "text": page.get_text()
            })
        doc.close()
        return pages
    
    @staticmethod
    def extract_images(pdf_path: str) -> List[Dict]:
        """Extract images from PDF"""
        doc = fitz.open(pdf_path)
        images = []
        
        for page_num, page in enumerate(doc):
            image_list = page.get_images()
            
            for img_index, img in enumerate(image_list):
                xref = img[0]
                base_image = doc.extract_image(xref)
                
                images.append({
                    "page": page_num + 1,
                    "index": img_index,
                    "image_data": base_image["image"],
                    "extension": base_image["ext"]
                })
        
        doc.close()
        return images
    
    @staticmethod
    def get_document_info(pdf_path: str) -> Dict:
        """Get PDF metadata"""
        doc = fitz.open(pdf_path)
        info = {
            "page_count": len(doc),
            "metadata": doc.metadata
        }
        doc.close()
        return info
