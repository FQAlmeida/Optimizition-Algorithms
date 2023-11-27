from math import inf
import pyomo.environ as pyo
from pyomo.opt import SolverFactory

model = pyo.ConcreteModel()


model.x = pyo.Var(domain=pyo.Reals, bounds=(-inf, 3))
model.y = pyo.Var(domain=pyo.Reals, bounds=(0, inf))

x = model.x
y = model.y

model.C1 = pyo.Constraint(expr=x + y <= 8)
model.C2 = pyo.Constraint(expr=8 * x + 3 * y >= -24)
model.C3 = pyo.Constraint(expr=-6 * x + 8 * y <= 48)
model.C4 = pyo.Constraint(expr=3 * x + 5 * y <= 15)
# model.C5 = pyo.Constraint(expr=x <= 3)
# model.C6 = pyo.Constraint(expr=y >= 0)

model.obj = pyo.Objective(expr=-4 * x - 2 * y, sense=pyo.minimize)

opt = SolverFactory("glpk")
opt.solve(model)

model.pprint()

x_value = pyo.value(x)
y_value = pyo.value(y)

print(f"x: {x_value}")
print(f"y: {y_value}")
