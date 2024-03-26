from django.db.models import Count
class MyAnnotation:
    def __init__(self,model_name,attribute_variable,variable_to_annotate):
        self.model_name = model_name
        self.attribute_variable = attribute_variable
        self.variable_to_annotate = variable_to_annotate
        
   
    def make_annotation(self):
        return self.model_name.objects.annotate(attribute_variable = Count(f'{self.variable_to_annotate}'))
        
    