import read, copy
from util import *
from logical_classes import *


class KnowledgeBase(object):
    def __init__(self, facts=[], rules=[]):
        self.facts = facts
        self.rules = rules

    def __repr__(self):
        return 'KnowledgeBase({!r}, {!r})'.format(self.facts, self.rules)

    def __str__(self):
        string = "Knowledge Base: \n"
        string += "\n".join((str(fact) for fact in self.facts)) + "\n"
        string += "\n".join((str(rule) for rule in self.rules))
        return string

    def kb_assert(self, fact):
        """Assert a fact or rule into the KB

        Args:
            fact (Fact or Rule): Fact or Rule we're asserting in the format produced by read.py
        """
        if isinstance(fact, Fact):
            if fact not in self.facts:
                self.facts.append(fact)
                print("Asserting {!r}".format(fact))
            else:
                print("Asserting failed. Reason: {!r} is already in the fact Knowledge Base".format(fact))
        elif isinstance(fact, Rule):
            if fact not in self.rules:
                self.rules.append(fact)
                print("Asserting {!r}".format(fact))
            else:
                print("Asserting failed. Reason: {!r} is already in the rules Knowledge Base".format(fact))
        else:
            print("Asserting failed. Reason: {!r} is not a fact or rule".format(fact))

        
    def kb_ask(self, fact):
        """Ask if a fact is in the KB

        Args:
            fact (Fact) - Fact to be asked

        Returns:
            ListOfBindings|False - ListOfBindings if result found, False otherwise
        """
        print("Asking {!r}".format(fact))
        count = 0

        if isinstance(fact, Fact):
            binds = ListOfBindings()
            for i in self.facts:
                j = match(fact.statement, i.statement)
                if j:
                    binds.add_bindings(j)
                    count += 1
            if count > 0:
                print("{!r} found".format(fact))
                return binds
            else:
                print("{!r} not found".format(fact))
                
        else:
            print("Asking failed. Reason: {!r} is not a fact".format(fact))



        
