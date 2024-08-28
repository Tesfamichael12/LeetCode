class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        row = [0] * len(image[0])
        for i in range(len(image)):
            image[i].reverse()
            for j in range(len(image)):
                if image[i][j] == 0: image[i][j] = 1
                else: image[i][j] = 0

        return image
