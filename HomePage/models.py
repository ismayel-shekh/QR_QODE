from django.db import models
from django.urls import reverse
import qrcode
from io import BytesIO
from django.core.files import File
import qrcode.constants


class User_all_data(models.Model):
    First_Name = models.CharField(max_length=100, blank = True, null= True)
    Last_Name = models.CharField(max_length=100, blank = True, null= True)
    phone_number = models.CharField(max_length=15, blank = True, null= True)
    qr_code = models.ImageField(upload_to='HomePage/media', blank= True, null= True)
    
    

    def __str__(self):
        return self.First_Name
    
    def save(self, *args, **kwargs):
        
        qr_data = f'First_Nmae: {self.First_Name}\nLast Name: {self.Last_Name}\nPhone Number: {self.phone_number}'
        
        qr = qrcode.QRCode(
            version = 1,
            error_correction = qrcode.constants.ERROR_CORRECT_L,
            box_size = 10,
            border = 4,
        )
        
        qr.add_data(qr_data)
        qr.make(fit = True)
        
        img = qr.make_image(fill_color ='black', back_color = 'white')
        buffer = BytesIO()
        img.save(buffer, format="PNG")
        file_name = f'{self.First_Name}_{self.Last_Name}_qr.png'
        self.qr_code.save(file_name, File(buffer), save=False)
        super().save(*args, **kwargs)        
        
        
        