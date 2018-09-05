from sklearn import tree

# Decision - Data moves in a direction based on a series of question then labels it.
# This label is the classification

X = [[181, 80, 44], [177, 70, 43], [160, 60, 38], [154, 54, 37], [166, 65, 40],
     [190, 90, 47], [175, 64, 39],[177, 70, 40], [159, 55, 37], [171, 75, 42],
     [181, 85, 43]]

Y = ['male', 'male', 'female', 'female', 'male', 'male', 'female', 'female',
     'female', 'male', 'male']

clf = tree.DecisionTreeClassifier()

clf = clf.fit(X,Y)

prediction_one = clf.predict([[190,88,45]])
prediction_two = clf.predict([[150,50,35]])
print(prediction_one)
print(prediction_two)
