import re
import paddleocr

def extract_yolo_output_text_with_paddleocr(output):
    try:
        detections = {}
        try: 
            for line in output.splitlines():
              match = re.match(r"(?P<name>\w+):\s+(?P<percentage>\d+)%\s+\(left_x:\s+(?P<left_x>\d+)\s+top_y:\s+(?P<top_y>\d+)\s+width:\s+(?P<width>\d+)\s+height:\s+(?P<height>\d+)\)", line)
              if match:
                class_name = match.group("name")
                bbox = (match.group("left_x"), match.group("top_y"), match.group("left_x") + match.group("width"), match.group("top_y") + match.group("height"))
                if class_name not in detections:
                  detections[class_name] = []
                detections[class_name].append((match.group("percentage"), bbox))
        except Exception as e:
            logger.info("")
        # Extract the bounding box with the highest percentage confidence.
        text_outputs = []

        try:
            for class_name, bounding_boxes in detections.items():
              highest_percentage = max(bounding_boxes, key=lambda x: x[0])[1]
              # Crop the image and extract the text from the bounding box using PaddleOCR.
              label_img = image.crop(highest_percentage)
              ocr = paddleocr.PaddleOCR(det_lang='ml', use_gpu=False, use_angle_cls=True, det_algorithm="DB")
              results = ocr.ocr(label_img)
          
              # Get the text from the OCR results.
              if results:
                text = results[0][0].get("text")
                text_outputs.append(text)
        except Exception as e:
            logger.info("")
      
        return text_outputs
    except Exception as e:
        logger.info("")

# Extract the text output from the YOLO model prediction using PaddleOCR.
text_outputs = extract_yolo_output_text_with_paddleocr(s_output)

# Print the text outputs.
for text_output in text_outputs:
  print(text_output)








import re
import paddleocr

def extract_yolo_output_text_with_paddleocr(output):
    try:
      detections = {}
      for line in output.splitlines():
        match = re.match(r"(?P<name>\w+):\s+(?P<percentage>\d+)%\s+\(left_x:\s+(?P<left_x>\d+)\s+top_y:\s+(?P<top_y>\d+)\s+width:\s+(?P<width>\d+)\s+height:\s+(?P<height>\d+)\)", line)
        if match:
          class_name = match.group("name")
          bbox = (match.group("left_x"), match.group("top_y"), match.group("left_x") + match.group("width"), match.group("top_y") + match.group("height"))
          percentage = int(match.group("percentage"))
          if class_name not in detections:
            detections[class_name] = []
          detections[class_name].append((percentage, bbox))
      # Extract the bounding box with the highest percentage confidence.
    except Exception e:
        logger.
    try:
      text_outputs = []
      for class_name, bounding_boxes in detections.items():
        highest_percentage = max(bounding_boxes, key=lambda x: x[0])[0]
        # Crop the image and extract the text from the bounding box using PaddleOCR.
        label_img = image.crop(highest_percentage)
        ocr = paddleocr.PaddleOCR(det_lang='ml', use_gpu=False, use_angle_cls=True, det_algorithm="DB")
        results = ocr.ocr(label_img)
    
        # Get the text from the OCR results.
        if results:
          text = results[0][0].get("text")
          text_outputs.append(text)
    except Exception as e:
        loggeer.
    
      return text_outputs

# Extract the text output from the YOLO model prediction using PaddleOCR.
text_outputs = extract_yolo_output_text_with_paddleocr(s_output)

# Print the text outputs.
for text_output in text_outputs:
  print(text_output)

