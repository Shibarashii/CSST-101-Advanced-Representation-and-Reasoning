# SCRIPT 

# Logical AND (∧)
def and_operation(p, q):
    """
    Perform logical conjunction (AND) on two boolean values.
    
    :param p: bool, first operand.
    :param q: bool, second operand.
    :return: bool, result of p AND q.
    """
    return p and q

# Logical OR (∨)
def or_operation(p, q):
    """
    Perform logical disjunction (OR) on two boolean values.
    
    :param p: bool, first operand.
    :param q: bool, second operand.
    :return: bool, result of p OR q.
    """
    return p or q

# Logical NOT (¬)
def not_operation(p):
    """
    Perform logical negation (NOT) on a boolean value.
    
    :param p: bool, operand.
    :return: bool, result of NOT p.
    """
    return not p

# Logical IMPLIES (→)
def implies_operation(p, q):
    """
    Perform logical implication (p → q).
    
    :param p: bool, antecedent.
    :param q: bool, consequent.
    :return: bool, result of p IMPLIES q.
    """
    return not p or q


def evaluate(statement, values):
    """
    Evaluate a logical statement based on given truth values.

    :param statement: str, logical expression using variables.
    :param values: dict, mapping variables to their truth values.
    :return: bool, evaluated truth value of the statement.
    """
    # Replace variable names with their corresponding boolean values
    for var, val in values.items():
        # Use word boundaries to avoid partial replacements
        statement = re.sub(rf'\b{var}\b', str(val), statement)
    
    # Replace logical operators to match Python syntax
    statement = statement.replace('AND', 'and').replace('OR', 'or').replace('NOT', 'not')

    try:
        # Evaluate the final expression
        return eval(statement)
    except SyntaxError as e:
        print(f"SyntaxError: {e}")
        return None

def forall(predicate, domain):
    """
    Check if a predicate is true for all elements in a domain.
    
    :param predicate: function, predicate to apply on elements.
    :param domain: list, elements over which to apply the predicate.
    :return: bool, True if predicate holds for all elements.
    """
    return all(predicate(x) for x in domain)

def exists(predicate, domain):
    """
    Check if a predicate is true for at least one element in a domain.
    
    :param predicate: function, predicate to apply on elements.
    :param domain: list, elements over which to apply the predicate.
    :return: bool, True if predicate holds for at least one element.
    """
    return any(predicate(x) for x in domain)


scenario = "environment" #@param ["game", "environment"] {allow-input: true}

class SimpleAI:
    def __init__(self, scenario):
        """
        Initialize the AI agent with a scenario.
        
        :param scenario: str, defines the context of decision-making.
        """
        self.scenario = scenario

    def decide(self, conditions):
        """
        Decide an action based on the current conditions and scenario.
        
        :param conditions: dict, mapping conditions to their truth values.
        :return: str, the chosen action.
        """
        if self.scenario == "game":
            if conditions['has_enemy']:
                return "Attack"
            elif conditions['has_resources']:
                return "Gather Resources"
            else:
                return "Explore"
        elif self.scenario == "environment":
            if conditions['weather'] == "rainy":
                return "Stay Inside"
            elif conditions['weather'] == "sunny":
                return "Go Out"
            else:
                return "Check Weather"
