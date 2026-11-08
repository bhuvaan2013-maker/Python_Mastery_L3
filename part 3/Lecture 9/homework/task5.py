class Camera:
    def __init__(self,megapixels):
        self.megapixels=megapixels
        self.photos_taken=0
    def take_photo(self):
        self.photos_taken=self.photos_taken+1
        print(f"Photo {self.photos_taken} taken at {self.megapixels} MP")
class Phone:
    def __init__(self,number):
        self.number=number
    def call_contact(self,name):
        print(f"Calling {name} from {self.number}")
class CameraPhone(Camera,Phone):
    def __init__(self,model,megapixels,number,photo_limit):
        Camera.__init__(self,megapixels)
        Phone.__init__(self,number)
        self.model=model
        self.photo_limit=photo_limit
    def shoot(self):
        if self.photo_limit==self.photos_taken:
            print(f"Storage Full")
        else:
            self.take_photo()
model=input()
megapixels=int(input())
number=input()
photo_limit=int(input())
no_photos=int(input())
name=input()
stroage=CameraPhone(model,megapixels,number,photo_limit)
for a in range(no_photos):
    stroage.shoot()
stroage.call_contact(name)
print(f"{stroage.model} saved {stroage.photos_taken} photos")