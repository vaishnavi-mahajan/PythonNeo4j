from py2neo import Graph, Node, Relationship
graph=Graph(password="Neo4j")
#graph.run("""create(liza:person{name:"liza"})""")

node1= Node("site", name="Amazon", )
graph.create(node1)
node2: Node= Node("sm", name="facebook")
graph.create(node2)
node3= Node("sm", name="instagram")
graph.create(node3)
node4= Node("sm", name="Email")
graph.create(node4)
node5= Node("sm", name="SMS")
graph.create(node5)
node6: Node= Node("sm", name="YouTube")
graph.create(node6)
node7= Node("person", name="35Peoples")
graph.create(node7)
node8= Node("person", name="40peoples")
graph.create(node8)
node9= Node("person", name="5Peoples")
graph.create(node9)
#node10= Node("person", name="8Peoples")
#graph.create(node10)
node11= Node("person", name="4Peoples")
graph.create(node11)
#node12= Node("person", name="1People")
#graph.create(node12)
#node13= Node("person", name="9Peoples")
#graph.create(node13)
node14= Node("person", name="85Peoples")
graph.create(node14)
#node15= Node("person", name="40Peoples")
#graph.create(node15)
node16= Node("offer", name="50% Off")
graph.create(node16)
node17= Node("offer", name="BUY1GET1")
graph.create(node17)
node18= Node("offer", name="70% Off")
graph.create(node18)
#node19= Node("person", name="16Poples")
#graph.create(node19)
node20= Node("person", name="3Peoples")
graph.create(node20)
node21= Node("person", name="2Peoples")
graph.create(node21)
#node22= Node("person", name="7Peoples")
#graph.create(node22)

relationship1=Relationship(node1, "SHOWS_ADDS" ,node2)
graph.create(relationship1)
relationship2=Relationship(node1, "SHOWS_ADDS" ,node3)
graph.create(relationship2)
relationship3=Relationship(node1, "SHOWS_ADDS" ,node4)
graph.create(relationship3)
relationship4=Relationship(node1, "SHOWS_ADDS" ,node5)
graph.create(relationship4)
relationship5=Relationship(node1, "SHOWS_ADDS" ,node6)
graph.create(relationship5)
relationship6=Relationship(node3, "Offer" ,node16)
graph.create(relationship6)
relationship7=Relationship(node3, "Offer" ,node17)
graph.create(relationship7)
relationship13=Relationship(node6, "Offer" ,node17)
graph.create(relationship13)
relationship14=Relationship(node16, "Views" ,node14)
graph.create(relationship14)
relationship15=Relationship(node8, "Bought_through_Youtube", node9)
graph.create(relationship15)
relationship8=Relationship(node18, "Views" ,node7)
graph.create(relationship8)
relationship9=Relationship(node17, "Views" ,node8)
graph.create(relationship9)
relationship10=Relationship(node7, "Bought_throuh_Instagram" ,node11)
graph.create(relationship10)
relationship22=Relationship(node14, "Bought_through_Facebook" ,node8)
graph.create(relationship22)
relationship23=Relationship(node14, "Bought_through_SMS" ,node21)
graph.create(relationship23)
#relationship11=Relationship(node16, "Views" ,node13)
#graph.create(relationship11)
relationship12=Relationship(node2, "Offer" ,node16)
graph.create(relationship12)
relationship13=Relationship(node14, "Bought_throuh_Facebook" ,node20)
graph.create(relationship13)
relationship14=Relationship(node5, "Offer" ,node16)
graph.create(relationship14)
#relationship15=Relationship(node2, "Offer" ,node17)
#graph.create(relationship15)
relationship16=Relationship(node3, "Offer" ,node17)
graph.create(relationship16)
relationship17=Relationship(node4, "Offer" ,node17)
graph.create(relationship17)
relationship18=Relationship(node2, "self" ,node2)
graph.create(relationship18)
relationship19=Relationship(node3, "Offer" ,node18)
graph.create(relationship19)
#relationship20=Relationship(node5, "Offer" ,node18)
#graph.create(relationship20)
relationship21=Relationship(node4, "Offer" ,node18)
graph.create(relationship21)
