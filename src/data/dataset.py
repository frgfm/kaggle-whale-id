# class to create a custom dataset
class Dataset:
    def __init__(self, csv_path, img_path, transform=None):
        """
        csv_path: path to csv file
        img_path: path to the image folder
        transform: torch transforms
        """
        # Transforms
        self.transforms = transform
        # Image folder path
        self.img_path = img_path
        # Ceate df from csv file
        self.data = pd.read_csv(csv_path)
        # Create array of images
        self.images = self.data.iloc[:, 0]
        # Create array of labels
        self.labels = self.data.iloc[:, 1]
        # Classes
        self.classes = set(self.labels)
        # Number of classes
        self.num_classes = len(self.classes)
        # label dictionaries
        self.label2int = dict((label, number) for number, label in enumerate(self.classes))
        self.int2label = dict(enumerate(self.label2int))

    def __len__(self):
        return len(self.data)

    def __getitem__(self, index):
        # Get image name from df
        image_name = os.path.join(self.img_path,
                               self.images[index])
        
        # Open image
        img = Image.open(image_name)
        # Transform image
        if self.transforms:
            img = self.transforms(img)
        # Get labels
        label = self.labels[index]
        sample = {'image': img, 'label': self.label2int[label]}

        
        return sample