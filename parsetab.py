
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'rightNOTleftIMPLIESIFFleftANDORAND IFF IMPLIES LPAREN NOT OR RPAREN VARIABLEexpression : VARIABLE\n                  | NOT expression\n                  | expression AND expression\n                  | expression OR expression\n                  | expression IMPLIES expression\n                  | expression IFF expression\n                  | LPAREN expression RPAREN\n                  | NOT LPAREN expression RPAREN'
    
_lr_action_items = {'VARIABLE':([0,3,4,5,6,7,8,10,],[2,2,2,2,2,2,2,2,]),'NOT':([0,3,4,5,6,7,8,10,],[3,3,3,3,3,3,3,3,]),'LPAREN':([0,3,4,5,6,7,8,10,],[4,10,4,4,4,4,4,4,]),'$end':([1,2,9,12,13,14,15,17,18,],[0,-1,-2,-3,-4,-5,-6,-7,-7,]),'AND':([1,2,9,11,12,13,14,15,16,17,18,],[5,-1,5,5,-3,-4,5,5,5,-7,-7,]),'OR':([1,2,9,11,12,13,14,15,16,17,18,],[6,-1,6,6,-3,-4,6,6,6,-7,-7,]),'IMPLIES':([1,2,9,11,12,13,14,15,16,17,18,],[7,-1,7,7,-3,-4,-5,-6,7,-7,-7,]),'IFF':([1,2,9,11,12,13,14,15,16,17,18,],[8,-1,8,8,-3,-4,-5,-6,8,-7,-7,]),'RPAREN':([2,9,11,12,13,14,15,16,17,18,],[-1,-2,17,-3,-4,-5,-6,18,-7,-7,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'expression':([0,3,4,5,6,7,8,10,],[1,9,11,12,13,14,15,16,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> expression","S'",1,None,None,None),
  ('expression -> VARIABLE','expression',1,'p_expression','Proyecto1Logica.py',32),
  ('expression -> NOT expression','expression',2,'p_expression','Proyecto1Logica.py',33),
  ('expression -> expression AND expression','expression',3,'p_expression','Proyecto1Logica.py',34),
  ('expression -> expression OR expression','expression',3,'p_expression','Proyecto1Logica.py',35),
  ('expression -> expression IMPLIES expression','expression',3,'p_expression','Proyecto1Logica.py',36),
  ('expression -> expression IFF expression','expression',3,'p_expression','Proyecto1Logica.py',37),
  ('expression -> LPAREN expression RPAREN','expression',3,'p_expression','Proyecto1Logica.py',38),
  ('expression -> NOT LPAREN expression RPAREN','expression',4,'p_expression','Proyecto1Logica.py',39),
]
