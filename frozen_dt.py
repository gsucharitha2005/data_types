#frozen datatype
#unorder,immutable,heterogenous data tpye

sports_room={"balls","measuring tapes","sports eqiments",1,2,3,4,("data",123)}
print(sports_room)
print(type(sports_room))
sports_room=frozenset(sports_room)
print(sports_room)
print(type(sports_room))