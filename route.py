def handleRoute(path,handlers):
    if(len(handlers)==0): return
    base, s, rest = path.partition("/")
    if(rest==""): return
    route, func = handlers[0]
    if rest.startswith(route): func(rest)
    else: handleRoute(path, handlers[1:])
