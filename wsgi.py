import numpy as np

print('Welcome to brick height calculator')
print()

def gen_bricklist():

  chartRange = list(range(1, 200))
  # chartRange = [*range(1, 50)]

  bclist = ['0']
  for k in chartRange:
  # for k in range(1, 50):
    rel7 = k*600
    rel6 = rel7 - 86
    rel5 = rel7 - 171
    rel4 = rel7 - 257
    rel3 = rel7 - 343
    rel2 = rel7 - 428
    rel1 = rel7 - 514
    bclist.append(rel1)
    bclist.append(rel2)
    bclist.append(rel3)
    bclist.append(rel4)
    bclist.append(rel5)
    bclist.append(rel6)
    bclist.append(rel7)
  # print(bclist)

  n = 0
  bchart = []
  while n <= len(bclist)-1:
    for k in bclist:
      k = f'{n}c: {k}'
      bchart.append(k)
      n += 1

  # print(bchart)

  displayRange = 250
  displayColumn = 5
  displayRow = int(displayRange / displayColumn)

  # x=np.array(a,b).reshape(c,d)

  chartArray = np.array(bchart[1:displayRange+1])
  chartArray = chartArray.reshape(displayColumn,displayRow)
  chartArray = np.rot90(np.fliplr(chartArray))
  chartArray = chartArray.tolist()

  # print(chartArray)


  brickchartHtml = "<table>\n"
  
  for k in chartArray:
    brickchartHtml += "  <tr>\n"
    for y in k:
      brickchartHtml += "    <td>{}</td>\n".format(y)
    brickchartHtml += "  </tr>\n"
  brickchartHtml += "</table>"

  return [bclist, brickchartHtml]

bclist, brickchartHtml = gen_bricklist()


# def gen_answer(arg):

#   while True:
    
#     # ques1 = (input('Enter 0 to end calc or\nEnter brick height: '))
#     ques1 = arg
    
#     if ques1 == 'l':
#       print('Brick Chart')
      

#     elif ques1 == '0':
#       print('Calculation ended')
#       break
    
#     else:
#       while True:
#         try:
#           print('')
#           print('{}c is: {}'.format(int(ques1), bclist[int(ques1)]))
#           print('')
#           break
          
#         except ValueError:
#           print("Oops!  That was no valid number. Try again...")
#           ques1 = (input('Enter 0 to end calc or\nEnter brick height: '))

#       ques2 = input('Plus plate? Please enter <Y> or leave blank: ')

#       if ques2 == 'Y':
#   #    print(bclist[int(ques1)]+35)
#         print('')
#         print('{}c + plate is: {}'.format(ques1, bclist[int(ques1)]+35))
#         print('')
    
#       elif ques2 == 'y':
#         print('')
#         print('{}c + plate is: {}'.format(ques1, bclist[int(ques1)]+35))
#         print('')
    
#       else:
#         print('')
#         print('{}c is: {}'.format(ques1, bclist[int(ques1)]))
#         print('')

mainHTML = ''
mainHTML += '''

<style>
table {
  font-family: arial narrow;
  border-collapse: collapse;
  width: 100%;
}

p {
  font-size: large;
  font-weight: bold;
  text-align: center;
}

span {
  font-size: x-large;
  color: red;
  font-weight: bold;
  text-align: center;
  display: block;
  margin-bottom: 20px;
}

td, th {
  border: 1px solid #dddddd;
  text-align: center;
  padding: 8px;
}

tr:nth-child(even) {
  background-color: #0077aa0f;
}
</style>

<body OnLoad="document.bchform.bch.focus();">
  <form name="bchform">
    <label for="bch">Enter coursing height (between 1c to 350c):</label>
    <input type="number" id="bch" name="bch" min="1" max="350">
    <input type="submit">
  </form>
<body>'''

from flask import Flask, request
app = Flask(__name__)

@app.route('/', methods=["GET"])

def input_form():

  if 'bch' not in request.args:
    return mainHTML + 'Please enter course height'

  else:
    bclist, brickchartHtml = gen_bricklist()
    bch = request.args['bch']
    return mainHTML + '<p> coursing height for ' + bch + 'c is: </p>' + '<span>' + str(bclist[int(bch)]) + '</span>' + '<p> Plate height: ' + str(bclist[int(bch)]+35) + '</p>'+ '<p> Soffit height: ' + str(bclist[int(bch)]-50
  ) + '</p>'+ brickchartHtml
        
   
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')