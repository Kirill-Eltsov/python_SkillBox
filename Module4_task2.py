from wtforms.validators import ValidationError
#Способ 1. Валидатор - функция
def phone_length(min_length, max_length, message=None):

    def validator(form, field):
        phone = str(field.data)
        if not (min_length <= len(phone) <= max_length):
            raise ValidationError(message or f"Phone number must be between {min_length} and {max_length} digits long.")

    return validator

#Способ 2. Валидатор - класс
class PhoneLength:
    def __init__(self, min_length, max_length, message=None):
        self.min_length = min_length
        self.max_length = max_length
        self.message = message

    def __call__(self, form, field):
        phone = str(field.data)
        if not (self.min_length <= len(phone) <= self.max_length):
           raise ValidationError(self.message or f"Phone number must be between {self.min_length} and {self.max_length} digits long.")