{"filter":false,"title":"models.py","tooltip":"/projects/myauthemail/models.py","undoManager":{"mark":9,"position":9,"stack":[[{"start":{"row":0,"column":0},"end":{"row":3,"column":0},"action":"remove","lines":["from django.db import models","","# Create your models here.",""],"id":2},{"start":{"row":0,"column":0},"end":{"row":14,"column":24},"action":"insert","lines":["\"\"\"Declare models for YOUR_APP app.\"\"\"","","from django.contrib.auth.models import AbstractUser","from django.db import models","from django.utils.translation import ugettext_lazy as _","","","class User(AbstractUser):","    \"\"\"User model.\"\"\"","","    username = None","    email = models.EmailField(_('email address'), unique=True)","","    USERNAME_FIELD = 'email'","    REQUIRED_FIELDS = []"]}],[{"start":{"row":0,"column":0},"end":{"row":0,"column":38},"action":"remove","lines":["\"\"\"Declare models for YOUR_APP app.\"\"\""],"id":3},{"start":{"row":0,"column":0},"end":{"row":1,"column":0},"action":"remove","lines":["",""]},{"start":{"row":0,"column":0},"end":{"row":1,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":4,"column":0},"end":{"row":35,"column":65},"action":"insert","lines":["class UserManager(BaseUserManager):","    \"\"\"Define a model manager for User model with no username field.\"\"\"","","    use_in_migrations = True","","    def _create_user(self, email, password, **extra_fields):","        \"\"\"Create and save a User with the given email and password.\"\"\"","        if not email:","            raise ValueError('The given email must be set')","        email = self.normalize_email(email)","        user = self.model(email=email, **extra_fields)","        user.set_password(password)","        user.save(using=self._db)","        return user","","    def create_user(self, email, password=None, **extra_fields):","        \"\"\"Create and save a regular User with the given email and password.\"\"\"","        extra_fields.setdefault('is_staff', False)","        extra_fields.setdefault('is_superuser', False)","        return self._create_user(email, password, **extra_fields)","","    def create_superuser(self, email, password, **extra_fields):","        \"\"\"Create and save a SuperUser with the given email and password.\"\"\"","        extra_fields.setdefault('is_staff', True)","        extra_fields.setdefault('is_superuser', True)","","        if extra_fields.get('is_staff') is not True:","            raise ValueError('Superuser must have is_staff=True.')","        if extra_fields.get('is_superuser') is not True:","            raise ValueError('Superuser must have is_superuser=True.')","","        return self._create_user(email, password, **extra_fields)"],"id":4}],[{"start":{"row":35,"column":65},"end":{"row":36,"column":0},"action":"insert","lines":["",""],"id":5},{"start":{"row":36,"column":0},"end":{"row":36,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":44,"column":24},"end":{"row":45,"column":0},"action":"insert","lines":["",""],"id":6},{"start":{"row":45,"column":0},"end":{"row":45,"column":4},"action":"insert","lines":["    "]},{"start":{"row":45,"column":4},"end":{"row":46,"column":0},"action":"insert","lines":["",""]},{"start":{"row":46,"column":0},"end":{"row":46,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":46,"column":4},"end":{"row":46,"column":27},"action":"insert","lines":["objects = UserManager()"],"id":7}],[{"start":{"row":46,"column":27},"end":{"row":47,"column":0},"action":"insert","lines":["",""],"id":8},{"start":{"row":47,"column":0},"end":{"row":47,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":0,"column":51},"end":{"row":0,"column":52},"action":"insert","lines":[","],"id":9}],[{"start":{"row":0,"column":52},"end":{"row":0,"column":53},"action":"insert","lines":[" "],"id":10}],[{"start":{"row":0,"column":53},"end":{"row":0,"column":68},"action":"insert","lines":["BaseUserManager"],"id":11}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":7,"column":28},"end":{"row":7,"column":28},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":66,"mode":"ace/mode/python"}},"timestamp":1530197980981,"hash":"4b6f48f0c0cfa08926f6c6f58531987017886fb4"}