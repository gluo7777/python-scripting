import parent,child1,child2

parent.logger.info("parent")
print(parent.logger.name)
child1.logger.info("child1")
print(child1.logger.name)
child2.logger.info("child2")
print(child2.logger.name)