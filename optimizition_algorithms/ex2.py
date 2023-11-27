import pyomo.environ as pyo
from pyomo.opt import SolverFactory

model = pyo.ConcreteModel()

model.x = pyo.Var(domain=pyo.Reals, bounds=(-5, 5))
model.y = pyo.Var(domain=pyo.Reals, bounds=(-5, 5))

x = model.x
y = model.y

model.obj = pyo.Objective(expr=pyo.cos(x + 1) + pyo.cos(x) * pyo.cos(y), sense=pyo.maximize)

opt = SolverFactory("ipopt")
opt.solve(model)

model.pprint()

x_value = pyo.value(x)
y_value = pyo.value(y)

print(f"x: {x_value}")
print(f"y: {y_value}")
