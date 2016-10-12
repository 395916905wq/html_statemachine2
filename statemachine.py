from string import upper
class StateMachine:
  def __init__(self):
      self.handlers = {}
      self.startState = None
      self.endStates = []

  def add_state(self, name, handler, end_state=0):
      name = upper(name)
      self.handlers[name] = handler
      if end_state:
           self.endStates.append(name)

  def set_start(self, name):
      self.startState = upper(name)

  def run(self, cargo):
      try:
         handler = self.handlers[self.startState]
      except:
         raise "InitializationError", "must call .set_start() before .run()"
      
      if not self.endStates:
         raise  "InitializationError", "at least one state must be an end_state"
      
      while True:
         (newstate, cargo) = handler(cargo)
         if upper(newstate) in self.endStates:
            print("reached ", newstate)
            break
         else:
            handler = self.handlers[upper(newstate)]