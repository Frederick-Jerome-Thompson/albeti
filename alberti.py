import random 

def getGeoWLetters(q,r):
  outerWheel = '1234ABCDEFGILMNOPQRSTVXZ'
  innerWheel = 'acegklnprtvz&xysomqihfdb'

  oLetter = outerWheel[q]
  iLetter = innerWheel[r]

  return oLetter,iLetter

def getGeoWDigits(x,n=24):
  q = x // n
  r = x % n

  return q,r

def getGeoWIndexes(oLetter,iLetter):
  outerWheel = '1234ABCDEFGILMNOPQRSTVXZ'
  innerWheel = 'acegklnprtvz&xysomqihfdb'

  q = outerWheel.find(oLetter)
  r = innerWheel.find(iLetter)

  return q,r




def getCWIndex(letter,wheel='1234ABCDEFGILMNOPQRSTVXZ'):
  q = wheel.find(letter)
  return q

def getCWLetter(index,wheel='acegklnprtvz&xysomqihfdb'):
  if index > len(wheel)-1:
    index = index % len(wheel)
  if index < 0:
    index = index + len(wheel)
  letter = wheel[index]
  return letter


def cleanCWText(theText,digitskey='RAND'):
  
  outerWheel = '1234ABCDEFGILMNOPQRSTVXZ'
  innerWheel = 'acegklnprtvz&xysomqihfdb'

  outerLetters = [letter for letter in outerWheel]


  theText = theText.upper()

  #Y,J -> I
  theText = theText.replace("Y","I")
  theText = theText.replace("J","I")

  #U,W -> V
  theText = theText.replace("U","V")
  theText = theText.replace("W","V")

  #H,K
  theText = theText.replace("H","G")
  theText = theText.replace("K","C")

  #add rotation key
  pos = -1 
  j=0
  period = len(digitskey)
  
  #random generation
  if digitskey == 'RAND':

    while True:
      pos = theText.find(' ', pos + 1)
      if pos == -1:
          break
      key_digit = random.randrange(1,4)
      theText = theText.replace(" ",str(key_digit),1)
      j = j +1
      j = j % period


  else:

    while True:
      pos = theText.find(' ', pos + 1)
      if pos == -1:
          break
      key_digit = digitskey[j]
      theText = theText.replace(" ",key_digit,1)
      j = j +1
      j = j % period


  aWordList = [letter for letter in theText if letter in outerWheel]
  newWord = ''.join(aWordList)

  return newWord


def cipherCWText(theText,startKey='Ql'):


  letters = [aLet for aLet in cleanCWText(theText)]
  letter_indexes =  [getCWIndex(letter) for letter in letters]

################get key set up

  oLet = startKey[0]
  iLet = startKey[1]
  oInd,iInd = getGeoWIndexes(oLet,iLet)
  offset = oInd - iInd
  

####################process encipherment

  cipher_letters = []

  for i, indx in enumerate(letter_indexes):
    clear_letter = letters[i]
    cipher_letter = getCWLetter(indx - offset)
    cipher_letters.append(cipher_letter)

    if clear_letter in ['1','2','3','4']:
      offset = offset + int(clear_letter)

  return "".join(cipher_letters)


def deCipherCWText(theText,startKey='Ql'):

  outerWheel = '1234ABCDEFGILMNOPQRSTVXZ'
  innerWheel = 'acegklnprtvz&xysomqihfdb'
  innerLetters = [letter for letter in innerWheel]

  letters = [aLet for aLet in theText if aLet in innerLetters]
  letter_indexes =  [getCWIndex(letter,wheel=innerWheel) for letter in letters]

################get key set up

  oLet = startKey[0]
  iLet = startKey[1]
  oInd,iInd = getGeoWIndexes(oLet,iLet)
  offset = iInd - oInd
  

####################process encipherment

  clear_letters = []

  for i, indx in enumerate(letter_indexes):
    cipher_letter = letters[i]
    clear_letter = getCWLetter(indx - offset,wheel=outerWheel)
    clear_letters.append(clear_letter)

    if clear_letter in ['1','2','3','4']:
      offset = offset - int(clear_letter)


  decipher_text = "".join(clear_letters)
  for num in ['1','2','3','4']:
    decipher_text = decipher_text.replace(num,' ')

  return decipher_text