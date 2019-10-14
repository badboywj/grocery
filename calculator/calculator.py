import wx
import re
import math
# begin wxGlade: extracode
# end wxGlade
ans=0
ts=""
class MyFrame(wx.Frame):
  def __init__(self, *args, **kwds):
    # begin wxGlade: MyFrame.__init__
    kwds["style"] = wx.DEFAULT_FRAME_STYLE
    wx.Frame.__init__(self, *args, **kwds)
    self.text_ctrl_1 = wx.TextCtrl(self, -1, "" ,style=wx.TE_READONLY)
    self.text_ctrl_2 = wx.TextCtrl(self, -1, "", style=wx.TE_READONLY)
    self.button_37 = wx.Button(self, -1, "7")
    self.button_38 = wx.Button(self, -1, "8")
    self.button_39 = wx.Button(self, -1, "9")
    self.button_40 = wx.Button(self, -1, "+")
    self.button_41 = wx.Button(self, -1, "-")
    self.button_42 = wx.Button(self, -1, "4")
    self.button_43 = wx.Button(self, -1, "5")
    self.button_44 = wx.Button(self, -1, "6")
    self.button_45 = wx.Button(self, -1, "x")
    self.button_46 = wx.Button(self, -1, "/")
    self.button_47 = wx.Button(self, -1, "1")
    self.button_48 = wx.Button(self, -1, "2")
    self.button_49 = wx.Button(self, -1, "3")
    self.button_50 = wx.Button(self, -1, "(")
    self.button_51 = wx.Button(self, -1, ")")
    self.button_52 = wx.Button(self, -1, "0")
    self.button_53 = wx.Button(self, -1, ".")
    self.button_54 = wx.Button(self, -1, "ans")
    self.button_55 = wx.Button(self, -1, "clear")
    self.button_56 = wx.Button(self, -1, "=")
    self.button_57 = wx.Button(self, -1, "pi")
    self.button_58 = wx.Button(self, -1, "e")
    self.button_59 = wx.Button(self, -1, "1/x")
    self.button_60 = wx.Button(self, -1, "x^2")
    self.button_61 = wx.Button(self, -1, "x^y")
    self.button_62 = wx.Button(self, -1, "sqrt")
    self.button_63 = wx.Button(self, -1, "sin")
    self.button_64 = wx.Button(self, -1, "cos")
    self.button_65 = wx.Button(self, -1, "tan")
    self.button_66 = wx.Button(self, -1, "log")
    self.button_67 = wx.Button(self, -1, "ln")
    self.button_68 = wx.Button(self, -1, "n!")
    self.button_69 = wx.Button(self, -1, "mod")
    self.button_70 = wx.Button(self, -1, "int")
    self.button_71 = wx.Button(self, -1, "yu")
    self.button_72 = wx.Button(self, -1, "|")
    self.button_73 = wx.Button(self, -1, "~")
    self.button_74 = wx.Button(self, -1, "xor")
    self.__set_properties()
    self.__do_layout()
    self.Bind(wx.EVT_BUTTON, self.bu37, self.button_37)
    self.Bind(wx.EVT_BUTTON, self.bu38, self.button_38)
    self.Bind(wx.EVT_BUTTON, self.bu39, self.button_39)
    self.Bind(wx.EVT_BUTTON, self.bu40, self.button_40)
    self.Bind(wx.EVT_BUTTON, self.bu41, self.button_41)
    self.Bind(wx.EVT_BUTTON, self.bu42, self.button_42)
    self.Bind(wx.EVT_BUTTON, self.bu43, self.button_43)
    self.Bind(wx.EVT_BUTTON, self.bu44, self.button_44)
    self.Bind(wx.EVT_BUTTON, self.bu45, self.button_45)
    self.Bind(wx.EVT_BUTTON, self.bu46, self.button_46)
    self.Bind(wx.EVT_BUTTON, self.bu47, self.button_47)
    self.Bind(wx.EVT_BUTTON, self.bu48, self.button_48)
    self.Bind(wx.EVT_BUTTON, self.bu49, self.button_49)
    self.Bind(wx.EVT_BUTTON, self.bu50, self.button_50)
    self.Bind(wx.EVT_BUTTON, self.bu51, self.button_51)
    self.Bind(wx.EVT_BUTTON, self.bu52, self.button_52)
    self.Bind(wx.EVT_BUTTON, self.bu53, self.button_53)
    self.Bind(wx.EVT_BUTTON, self.bu54, self.button_54)
    self.Bind(wx.EVT_BUTTON, self.bu55, self.button_55)
    self.Bind(wx.EVT_BUTTON, self.bu56, self.button_56)
    self.Bind(wx.EVT_BUTTON, self.bu57, self.button_57)
    self.Bind(wx.EVT_BUTTON, self.bu58, self.button_58)
    self.Bind(wx.EVT_BUTTON, self.bu59, self.button_59)
    self.Bind(wx.EVT_BUTTON, self.bu60, self.button_60)
    self.Bind(wx.EVT_BUTTON, self.bu61, self.button_61)
    self.Bind(wx.EVT_BUTTON, self.bu62, self.button_62)
    self.Bind(wx.EVT_BUTTON, self.bu63, self.button_63)
    self.Bind(wx.EVT_BUTTON, self.bu64, self.button_64)
    self.Bind(wx.EVT_BUTTON, self.bu65, self.button_65)
    self.Bind(wx.EVT_BUTTON, self.bu66, self.button_66)
    self.Bind(wx.EVT_BUTTON, self.bu67, self.button_67)
    self.Bind(wx.EVT_BUTTON, self.bu68, self.button_68)
    self.Bind(wx.EVT_BUTTON, self.bu69, self.button_69)
    self.Bind(wx.EVT_BUTTON, self.bu70, self.button_70)
    self.Bind(wx.EVT_BUTTON, self.bu71, self.button_71)
    self.Bind(wx.EVT_BUTTON, self.bu72, self.button_72)
    self.Bind(wx.EVT_BUTTON, self.bu73, self.button_73)
    self.Bind(wx.EVT_BUTTON, self.bu74, self.button_74)
    # end wxGlade
    self.Show(True)
  def __set_properties(self):
    # begin wxGlade: MyFrame.__set_properties
    self.SetTitle("Python Calculater by CYG")
    self.text_ctrl_1.SetMinSize((500, 30))
    self.text_ctrl_2.SetMinSize((500, 50))
    self.button_37.SetMinSize((100, 60))
    self.button_38.SetMinSize((100, 60))
    self.button_39.SetMinSize((100, 60))
    self.button_40.SetMinSize((100, 60))
    self.button_41.SetMinSize((100, 60))
    self.button_42.SetMinSize((100, 60))
    self.button_43.SetMinSize((100, 60))
    self.button_44.SetMinSize((100, 60))
    self.button_46.SetMinSize((100, 60))
    self.button_45.SetMinSize((100, 60))
    self.button_47.SetMinSize((100, 60))
    self.button_48.SetMinSize((100, 60))
    self.button_49.SetMinSize((100, 60))
    self.button_50.SetMinSize((100, 60))
    self.button_51.SetMinSize((100, 60))
    self.button_52.SetMinSize((100, 60))
    self.button_53.SetMinSize((100, 60))
    self.button_54.SetMinSize((100, 60))
    self.button_55.SetMinSize((100, 60))
    self.button_56.SetMinSize((100, 60))
    self.button_57.SetMinSize((83, 50))
    self.button_58.SetMinSize((83, 50))
    self.button_59.SetMinSize((83, 50))
    self.button_60.SetMinSize((83, 50))
    self.button_61.SetMinSize((83, 50))
    self.button_62.SetMinSize((83, 50))
    self.button_63.SetMinSize((83, 50))
    self.button_64.SetMinSize((83, 50))
    self.button_65.SetMinSize((83, 50))
    self.button_66.SetMinSize((83, 50))
    self.button_67.SetMinSize((83, 50))
    self.button_68.SetMinSize((83, 50))
    self.button_69.SetMinSize((83, 50))
    self.button_70.SetMinSize((83, 50))
    self.button_71.SetMinSize((83, 50))
    self.button_72.SetMinSize((83, 50))
    self.button_73.SetMinSize((83, 50))
    self.button_74.SetMinSize((83, 50))
    # end wxGlade
  def __do_layout(self):
    # begin wxGlade: MyFrame.__do_layout
    sizer_2 = wx.BoxSizer(wx.VERTICAL)
    sizer_3 = wx.BoxSizer(wx.VERTICAL)
    grid_sizer_1 = wx.GridSizer(4, 5, 0, 0)
    grid_sizer_2 = wx.GridSizer(3, 6, 0, 0)
    sizer_3.Add(self.text_ctrl_2, 0, 0, 0)
    sizer_3.Add(self.text_ctrl_1, 0, 0, 0)
    grid_sizer_1.Add(self.button_37, 0, 0, 0)
    grid_sizer_1.Add(self.button_38, 0, 0, 0)
    grid_sizer_1.Add(self.button_39, 0, 0, 0)
    grid_sizer_1.Add(self.button_40, 0, 0, 0)
    grid_sizer_1.Add(self.button_41, 0, 0, 0)
    grid_sizer_1.Add(self.button_42, 0, 0, 0)
    grid_sizer_1.Add(self.button_43, 0, 0, 0)
    grid_sizer_1.Add(self.button_44, 0, 0, 0)
    grid_sizer_1.Add(self.button_45, 0, 0, 0)
    grid_sizer_1.Add(self.button_46, 0, 0, 0)
    grid_sizer_1.Add(self.button_47, 0, 0, 0)
    grid_sizer_1.Add(self.button_48, 0, 0, 0)
    grid_sizer_1.Add(self.button_49, 0, 0, 0)
    grid_sizer_1.Add(self.button_50, 0, 0, 0)
    grid_sizer_1.Add(self.button_51, 0, 0, 0)
    grid_sizer_1.Add(self.button_52, 0, 0, 0)
    grid_sizer_1.Add(self.button_53, 0, 0, 0)
    grid_sizer_1.Add(self.button_54, 0, 0, 0)
    grid_sizer_1.Add(self.button_55, 0, 0, 0)
    grid_sizer_1.Add(self.button_56, 0, 0, 0)
    grid_sizer_2.Add(self.button_57, 0, 0, 0)
    grid_sizer_2.Add(self.button_58, 0, 0, 0)
    grid_sizer_2.Add(self.button_59, 0, 0, 0)
    grid_sizer_2.Add(self.button_60, 0, 0, 0)
    grid_sizer_2.Add(self.button_61, 0, 0, 0)
    grid_sizer_2.Add(self.button_62, 0, 0, 0)
    grid_sizer_2.Add(self.button_63, 0, 0, 0)
    grid_sizer_2.Add(self.button_64, 0, 0, 0)
    grid_sizer_2.Add(self.button_65, 0, 0, 0)
    grid_sizer_2.Add(self.button_66, 0, 0, 0)
    grid_sizer_2.Add(self.button_67, 0, 0, 0)
    grid_sizer_2.Add(self.button_68, 0, 0, 0)
    grid_sizer_2.Add(self.button_69, 0, 0, 0)
    grid_sizer_2.Add(self.button_70, 0, 0, 0)
    grid_sizer_2.Add(self.button_71, 0, 0, 0)
    grid_sizer_2.Add(self.button_72, 0, 0, 0)
    grid_sizer_2.Add(self.button_73, 0, 0, 0)
    grid_sizer_2.Add(self.button_74, 0, 0, 0)
    sizer_3.Add(grid_sizer_1, 1, wx.EXPAND, 0)
    sizer_3.Add(grid_sizer_2, 1, wx.EXPAND, 0)
    sizer_2.Add(sizer_3, 1, wx.EXPAND, 0)
    self.SetSizer(sizer_2)
    sizer_2.Fit(self)
    self.Layout()
    # end wxGlade
  def bu37(self, event): # wxGlade: MyFrame.<event_handler>
    global ts
    ts+="7"
    self.text_ctrl_1.AppendText("7")
    event.Skip()
  def bu38(self, event): # wxGlade: MyFrame.<event_handler>
    global ts
    ts+="8"
    self.text_ctrl_1.AppendText("8")
    event.Skip()
  def bu39(self, event): # wxGlade: MyFrame.<event_handler>
    global ts
    ts += "9"
    self.text_ctrl_1.AppendText("9")
    event.Skip()
  def bu40(self, event): # wxGlade: MyFrame.<event_handler>
    global ts
    ts += "+"
    self.text_ctrl_1.AppendText("+")
    event.Skip()
  def bu41(self, event): # wxGlade: MyFrame.<event_handler>
    global ts
    ts += "-"
    self.text_ctrl_1.AppendText("-")
    event.Skip()
  def bu42(self, event): # wxGlade: MyFrame.<event_handler>
    global ts
    ts += "4"
    self.text_ctrl_1.AppendText("4")
    event.Skip()
  def bu43(self, event): # wxGlade: MyFrame.<event_handler>
    global ts
    ts += "5"
    self.text_ctrl_1.AppendText("5")
    event.Skip()
  def bu44(self, event): # wxGlade: MyFrame.<event_handler>
    global ts
    ts += "6"
    self.text_ctrl_1.AppendText("6")
    event.Skip()
  def bu45(self, event): # wxGlade: MyFrame.<event_handler>
    global ts
    ts += "*"
    self.text_ctrl_1.AppendText("*")
    event.Skip()
  def bu46(self, event): # wxGlade: MyFrame.<event_handler>
    global ts
    ts += "/"
    self.text_ctrl_1.AppendText("/")
    event.Skip()
  def bu47(self, event): # wxGlade: MyFrame.<event_handler>
    global ts
    ts += "1"
    self.text_ctrl_1.AppendText("1")
    event.Skip()
  def bu48(self, event): # wxGlade: MyFrame.<event_handler>
    global ts
    ts += "2"
    self.text_ctrl_1.AppendText("2")
    event.Skip()
  def bu49(self, event): # wxGlade: MyFrame.<event_handler>
    global ts
    ts += "3"
    self.text_ctrl_1.AppendText("3")
    event.Skip()
  def bu50(self, event): # wxGlade: MyFrame.<event_handler>
    global ts
    ts += "("
    self.text_ctrl_1.AppendText("(")
    event.Skip()
  def bu51(self, event): # wxGlade: MyFrame.<event_handler>
    global ts
    ts += ")"
    self.text_ctrl_1.AppendText(")")
    event.Skip()
  def bu52(self, event): # wxGlade: MyFrame.<event_handler>
    global ts
    ts += "0"
    self.text_ctrl_1.AppendText("0")
    event.Skip()
  def bu53(self, event): # wxGlade: MyFrame.<event_handler>
    global ts
    ts += "."
    self.text_ctrl_1.AppendText(".")
    event.Skip()
  def bu54(self, event): # wxGlade: MyFrame.<event_handler>
    global ts
    ts += "ans"
    self.text_ctrl_1.AppendText("ans")
    event.Skip()
  def bu55(self, event): # wxGlade: MyFrame.<event_handler>
    global ts
    self.text_ctrl_1.Clear()
    self.text_ctrl_2.Clear()
    ans=0
    ts=""
    event.Skip()
  def minus_operation(self,expresstion):
    minus_operators = re.split("-", expresstion)
    calc_list = re.findall("[0-9]", expresstion)
    if minus_operators[0] == "":
      calc_list[0] = '-%s' % calc_list[0]
    res = reduce(lambda x, y: float(x) - float(y), calc_list)
    return res
  def del_duplicates(self,ts):
    ts = ts.replace("++", "+")
    ts = ts.replace("--", "-")
    ts = ts.replace("+-", "-")
    ts = ts.replace("--", "+")
    ts = ts.replace('- -', "+")
    return ts
  def mutiply_dividend(self,expresstion):
    calc_list = re.split("[*/]", expresstion)
    operators = re.findall("[*/]", expresstion)
    res = None
    for index, i in enumerate(calc_list):
      if res:
        if operators[index - 1] == '*':
          res *= float(i)
        elif operators[index - 1] == '/':
          res /= float(i)
      else:
        res = float(i)
    return res
  def special_features(self,plus_and_minus_operators, multiply_and_dividend):
    for index, i in enumerate(multiply_and_dividend):
      i = i.strip()
      if i.endswith("*") or i.endswith("/"):
        multiply_and_dividend[index] = multiply_and_dividend[index] + plus_and_minus_operators[index] + \
                        multiply_and_dividend[index + 1]
        del multiply_and_dividend[index + 1]
        del plus_and_minus_operators[index]
    return plus_and_minus_operators, multiply_and_dividend
  def minus_special(self,operator_list, calc_list):
    for index, i in enumerate(calc_list):
      if i == '':
        calc_list[index + 1] = i + calc_list[index + 1].strip()
  def figure_up(self,ts):
    ts = ts.strip("()")
    ts = self.del_duplicates(ts)
    plus_and_minus_operators = re.findall("[+-]", ts)
    multiply_and_dividend = re.split("[+-]", ts)
    if len(multiply_and_dividend[0].strip()) == 0:
      multiply_and_dividend[1] = plus_and_minus_operators[0] + multiply_and_dividend[1]
      del multiply_and_dividend[0]
      del plus_and_minus_operators[0]
    plus_and_minus_operators, multiply_and_dividend = self.special_features(plus_and_minus_operators,
                                      multiply_and_dividend)
    for index, i in enumerate(multiply_and_dividend):
      if re.search("[*/]", i):
        sub_res = self.mutiply_dividend(i)
        multiply_and_dividend[index] = sub_res
    #print(multiply_and_dividend, plus_and_minus_operators)
    final_res = None
    for index, item in enumerate(multiply_and_dividend):
      if final_res:
        if plus_and_minus_operators[index - 1] == '+':
          final_res += float(item)
        elif plus_and_minus_operators[index - 1] == '-':
          final_res -= float(item)
      else:
        final_res = float(item)
    return final_res
  def bu56(self, event): # wxGlade: MyFrame.<event_handler>
    global ans
    global ts
    if re.search("pi", ts):
      lists = re.findall("pi", ts)
      for i in range(0, len(lists)):
        te = str(math.pi)
        self.text_ctrl_2.SetValue(te)
        ts = re.sub("pi", te, ts, 1)
        #self.text_ctrl_1.SetValue(ts)
    if re.search("e", ts):
      lists = re.findall("e", ts)
      for i in range(0, len(lists)):
        te = str(math.e)
        self.text_ctrl_2.SetValue(te)
        ts = re.sub("e", te, ts, 1)
        #self.text_ctrl_1.SetValue(ts)
    if re.search("sin.*\)",ts):
      lists=re.findall("sin(.+?)",ts)
      for i in range(0,len(lists)):
        te=float(lists[i])
        te=str(math.sin(te))
        self.text_ctrl_2.SetValue(te)
        ts=re.sub("sin.*?\)",te,ts,1)
        #self.text_ctrl_1.SetValue(ts)
    if re.search("cos.*\)", ts):
      lists = re.findall("cos(.+?)", ts)
      for i in range(0, len(lists)):
        te = float(lists[i])
        te = str(math.cos(te))
        self.text_ctrl_2.SetValue(te)
        ts = re.sub("cos.*?\)", te, ts, 1)
        #self.text_ctrl_1.SetValue(ts)
    if re.search("tan.*\)", ts):
      lists = re.findall("tan(.+?)", ts)
      for i in range(0, len(lists)):
        te = float(lists[i])
        te = str(math.tan(te))
        self.text_ctrl_2.SetValue(te)
        ts = re.sub("tan.*?\)", te, ts, 1)
        #self.text_ctrl_1.SetValue(ts)
    if re.search("ln.*\)", ts):
      lists = re.findall("ln(.+?)", ts)
      for i in range(0, len(lists)):
        te = float(lists[i])
        te = str(math.log(te))
        self.text_ctrl_2.SetValue(te)
        ts = re.sub("ln.*?\)", te, ts, 1)
        #self.text_ctrl_1.SetValue(ts)
    if re.search("log.*\)", ts):
      lists = re.findall("log(.+?)", ts)
      for i in range(0, len(lists)):
        te = float(lists[i])
        te = str(math.log(te)/math.log(10))
        self.text_ctrl_2.SetValue(te)
        ts = re.sub("log.*?\)", te, ts, 1)
        #self.text_ctrl_1.SetValue(ts)
    if re.search("sqrt.*\)", ts):
      lists = re.findall("sqrt(.+?)", ts)
      for i in range(0, len(lists)):
        te = float(lists[i])
        te = str(math.sqrt(te))
        self.text_ctrl_2.SetValue(te)
        ts = re.sub("sqrt.*?\)", te, ts, 1)
        #self.text_ctrl_1.SetValue(ts)
    if re.search("int.*\)", ts):
      lists = re.findall("int(.+?)", ts)
      for i in range(0, len(lists)):
        te=float(lists[i])
        te=int(te)
        te = str(te)
        self.text_ctrl_2.SetValue(te)
        ts = re.sub("int.*?\)", te, ts, 1)
        #self.text_ctrl_1.SetValue(ts)
    if re.search("ans", ts):
      lists = re.findall("ans", ts)
      for i in range(0, len(lists)):
        te = str(ans)
        self.text_ctrl_2.SetValue(te)
        ts = re.sub("ans", te, ts, 1)
        #self.text_ctrl_1.SetValue(ts)
    if re.search("?−?\d∗\.?\d∗?\^?−?\d∗\.?\d∗?", ts):
      lists1 = re.findall("?(−?\d∗\.?\d∗?)?\^", ts)
      lists2 = re.findall("\^?(−?\d∗\.?\d∗)?", ts)
      for i in range(0, len(lists1)):
        te1=float(lists1[i])
        te2=float(lists2[i])
        #print te1
        #print te2
        te=math.pow(te1,te2)
        te = str(te)
        self.text_ctrl_2.SetValue(te)
        ts = re.sub("?[0−9]∗\.?[0−9]∗??\^?[0−9]∗\.?[0−9]∗?", te, ts, 1)
        #self.text_ctrl_1.SetValue(ts)
      #ts = re.sub("?−?\d∗\.?\d∗?\^?−?\d∗\.?\d∗??", te, ts, 1)
    if re.search("?−?\d∗?\!", ts):
        lists = re.findall("?(−?\d+?)?\!", ts)
        for i in range(0, len(lists)):
          te = float(lists[i])
          te = math.factorial(te)
          te = str(te)
          self.text_ctrl_2.SetValue(te)
          ts = re.sub("?−?\d+??\!", te, ts, 1)
          #self.text_ctrl_1.SetValue(ts)
    #print ts
    flag=True
    while flag:
      m = re.search("[()]∗", ts)
      if m:
        sub_res=self.figure_up(m.group())
        ts=ts.replace(m.group(),str(sub_res))
      else:
        ans=self.figure_up(ts)
        flag=False
    self.text_ctrl_2.SetValue(str(ans))
      #ans=
    #self.text_ctrl_2.SetValue(str(ans))
    # self.text_ctrl_1.Clear()
    event.Skip()
  def bu57(self, event): # wxGlade: MyFrame.<event_handler>
    global ts
    ts += "pi"
    self.text_ctrl_1.AppendText("pi")
    event.Skip()
  def bu58(self, event): # wxGlade: MyFrame.<event_handler>
    global ts
    ts += "e"
    self.text_ctrl_1.AppendText("e")
    event.Skip()
  def bu59(self, event): # wxGlade: MyFrame.<event_handler>
    global ts
    ts += "^(-1)"
    self.text_ctrl_1.AppendText("^(-1)")
    event.Skip()
  def bu60(self, event): # wxGlade: MyFrame.<event_handler>
    global ts
    ts += "^2"
    self.text_ctrl_1.AppendText("^2")
    event.Skip()
  def bu61(self, event): # wxGlade: MyFrame.<event_handler>
    global ts
    ts += "^"
    self.text_ctrl_1.AppendText("^")
    event.Skip()
  def bu62(self, event): # wxGlade: MyFrame.<event_handler>
    global ts
    ts += "sqrt("
    self.text_ctrl_1.AppendText("sqrt(")
    event.Skip()
  def bu63(self, event): # wxGlade: MyFrame.<event_handler>
    global ts
    ts += "sin("
    self.text_ctrl_1.AppendText("sin(")
    event.Skip()
  def bu64(self, event): # wxGlade: MyFrame.<event_handler>
    global ts
    ts += "cos("
    self.text_ctrl_1.AppendText("cos(")
    event.Skip()
  def bu65(self, event): # wxGlade: MyFrame# .<event_handler>
    global ts
    ts += "tan("
    self.text_ctrl_1.AppendText("tan(")
    event.Skip()
  def bu66(self, event): # wxGlade: MyFrame.<event_handler>
    global ts
    ts += "log("
    self.text_ctrl_1.AppendText("log(")
    event.Skip()
  def bu67(self, event): # wxGlade: MyFrame.<event_handler>
    global ts
    ts += "ln("
    self.text_ctrl_1.AppendText("ln(")
    event.Skip()
  def bu68(self, event): # wxGlade: MyFrame.<event_handler>
    global ts
    ts += "!"
    self.text_ctrl_1.AppendText("!")
    event.Skip()
  def bu69(self, event): # wxGlade: MyFrame.<event_handler>
    global ts
    ts += "m"
    self.text_ctrl_1.AppendText("m")#qumo
    event.Skip()
  def bu70(self, event): # wxGlade: MyFrame.<event_handler>
    global ts
    ts += "int("
    self.text_ctrl_1.AppendText("int(")
    event.Skip()
  def bu71(self, event): # wxGlade: MyFrame.<event_handler>
    global ts
    ts += "u"
    self.text_ctrl_1.AppendText("u")#yu
    event.Skip()
  def bu72(self, event): # wxGlade: MyFrame.<event_handler>
    global ts
    ts += "|"
    self.text_ctrl_1.AppendText("|")#huo
    event.Skip()
  def bu73(self, event): # wxGlade: MyFrame.<event_handler>
    global ts
    ts += "n("
    self.text_ctrl_1.AppendText("n(")#fei
    event.Skip()
  def bu74(self, event): # wxGlade: MyFrame.<event_handler>
    global ts
    ts += "x"
    self.text_ctrl_1.AppendText("x")#yihuo
    event.Skip()
    # end of class MyFrame
if __name__ == "__main__":
  app=wx.App(False)
  myframe= MyFrame(None)
  app.MainLoop()
