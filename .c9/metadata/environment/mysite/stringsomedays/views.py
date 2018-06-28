{"changed":true,"filter":false,"title":"views.py","tooltip":"/mysite/stringsomedays/views.py","value":"from django.shortcuts import get_object_or_404, render\nfrom django.http import HttpResponseRedirect\nfrom django.urls import reverse\nfrom django.views import generic\n\nfrom .models import *\n\n\nclass IndexView(generic.ListView):\n    template_name = 'stringsomedays/index.html'\n\n    def get_queryset(self):\n        return \"Doodoobacon\"\n","undoManager":{"mark":8,"position":9,"stack":[[{"start":{"row":10,"column":0},"end":{"row":11,"column":0},"action":"insert","lines":["",""],"id":2}],[{"start":{"row":11,"column":0},"end":{"row":13,"column":57},"action":"insert","lines":["def get_queryset(self):","        \"\"\"Return the last five published questions.\"\"\"","        return Question.objects.order_by('-pub_date')[:5]"],"id":3}],[{"start":{"row":11,"column":0},"end":{"row":11,"column":4},"action":"insert","lines":["    "],"id":4}],[{"start":{"row":13,"column":15},"end":{"row":13,"column":57},"action":"remove","lines":["Question.objects.order_by('-pub_date')[:5]"],"id":5},{"start":{"row":13,"column":15},"end":{"row":13,"column":16},"action":"insert","lines":["\""]},{"start":{"row":13,"column":16},"end":{"row":13,"column":17},"action":"insert","lines":["D"]},{"start":{"row":13,"column":17},"end":{"row":13,"column":18},"action":"insert","lines":["e"]},{"start":{"row":13,"column":18},"end":{"row":13,"column":19},"action":"insert","lines":["e"]}],[{"start":{"row":13,"column":18},"end":{"row":13,"column":19},"action":"remove","lines":["e"],"id":6},{"start":{"row":13,"column":17},"end":{"row":13,"column":18},"action":"remove","lines":["e"]}],[{"start":{"row":13,"column":17},"end":{"row":13,"column":18},"action":"insert","lines":["o"],"id":7},{"start":{"row":13,"column":18},"end":{"row":13,"column":19},"action":"insert","lines":["o"]},{"start":{"row":13,"column":19},"end":{"row":13,"column":20},"action":"insert","lines":["d"]},{"start":{"row":13,"column":20},"end":{"row":13,"column":21},"action":"insert","lines":["o"]},{"start":{"row":13,"column":21},"end":{"row":13,"column":22},"action":"insert","lines":["o"]},{"start":{"row":13,"column":22},"end":{"row":13,"column":23},"action":"insert","lines":["b"]}],[{"start":{"row":13,"column":23},"end":{"row":13,"column":24},"action":"insert","lines":["a"],"id":8},{"start":{"row":13,"column":24},"end":{"row":13,"column":25},"action":"insert","lines":["c"]},{"start":{"row":13,"column":25},"end":{"row":13,"column":26},"action":"insert","lines":["o"]},{"start":{"row":13,"column":26},"end":{"row":13,"column":27},"action":"insert","lines":["n"]},{"start":{"row":13,"column":27},"end":{"row":13,"column":28},"action":"insert","lines":["\""]}],[{"start":{"row":13,"column":28},"end":{"row":14,"column":0},"action":"insert","lines":["",""],"id":9},{"start":{"row":14,"column":0},"end":{"row":14,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":14,"column":4},"end":{"row":14,"column":8},"action":"remove","lines":["    "],"id":10},{"start":{"row":14,"column":0},"end":{"row":14,"column":4},"action":"remove","lines":["    "]}],[{"start":{"row":12,"column":8},"end":{"row":12,"column":55},"action":"remove","lines":["\"\"\"Return the last five published questions.\"\"\""],"id":11},{"start":{"row":12,"column":4},"end":{"row":12,"column":8},"action":"remove","lines":["    "]},{"start":{"row":12,"column":0},"end":{"row":12,"column":4},"action":"remove","lines":["    "]},{"start":{"row":11,"column":27},"end":{"row":12,"column":0},"action":"remove","lines":["",""]}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":11,"column":27},"end":{"row":11,"column":27},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":32,"mode":"ace/mode/python"}},"timestamp":1529685852460}