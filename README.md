# Coco_Converter

Merge Coco (Json) datasets of 2 different customers

## Requirments
`python==3.x`

## Installation
```
Simply:
1- git clone https://github.com/xgen-dev/coco_converter.git
2- cd coco_converter
```

## Merge Instructions

1. install python libraries: tqdm and pycocotools needed
2. place 2 COCO files that need to be merged in the coco_converter folder
3. In terminal, run:
```
python merge.py Json1.json Json2.json output.json
```
- Json1.json and Json2.json are the two COCO files to be merged.
- output.json is the output file of the merged results

4. check id correctness:
```
python print_test.py
```
- idCheck gives negative result when ids are not start with 0, OR there are duplicated ids, OR any previous id is not exactly 1 smaller

*Note: the script will do the necessary checks as well (duplicate filenames, ....)*
# coco-converter
