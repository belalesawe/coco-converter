# install libraries as needed
from pycocotools.coco import COCO

annFile='./output.json'

# Initialize the COCO api for instance annotations
coco=COCO(annFile)

# get all ids of categories
# Load the categories in a variable to ready for print
catIDs = coco.getCatIds()
cats = coco.loadCats(catIDs)
#print(cats)

# Load the images in a variable
imgIDs = coco.getImgIds()
imgs = coco.loadImgs(imgIDs)

# Load the annotations in a variable
annIDs = coco.getAnnIds()
anns = coco.loadAnns(annIDs)





# idCheck function checks id correctness after merging
#         returns False when id is not start with 0
#                       when there are duplicated ids
#                       when previous id is not exactly 1 smaller
#         returns True  when add ids are good
def idCheck(ids):
    n = len(ids)
    for i in range(n):
        if (i != ids[i]):
            return False
    return True

# print test result
print('\n---------- idCheck result ----------')
print('\n>> idCheck for categories passed: ', idCheck(catIDs), '\n', len(catIDs), ' categories in total')
print('\n>> idCheck for images passed: ', idCheck(imgIDs), '\n', len(imgIDs), ' images in total')
print('\n>> idCheck for annotations passed: ', idCheck(annIDs), '\n', len(annIDs), ' annotations in total')
