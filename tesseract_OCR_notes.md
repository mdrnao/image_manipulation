# Tesseract OCR CLI command

[Tesseract CLI options](https://github.com/tesseract-ocr/tesseract/blob/main/doc/tesseract.1.asc)

```tesseract $cropped_img output --oem 3 -l eng --psm 6 -c edges_childarea=0.2'```

1. ```$cropped_img``` - the image file you want to process
2. ```output``` - the name of the output file, default a .txt file
3. ```-oem 3``` - the OCR engine. 3 is default.
4. ```-l eng``` - the language (eng is english!)
5. ```--psm 6``` - the layout, 6 means sssume a single uniform block of text.
6. ```-c parameter=0``` - add any number of parameters you wish to change here. Pretty sure it's unlimited. 


