from sklearn import tree
model=tree.DecisionTreeClassifier(criterion="entropy")
model.fit(x,y)