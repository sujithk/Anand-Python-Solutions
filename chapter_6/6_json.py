def json_encode(data):
    if isinstance(data, bool):
        if data:
            return "true"
        else:
            return "false"
    elif isinstance(data, (int, float)):
        return str(data)
    elif isinstance(data, str):
        return '"' + escape_string(data) + '"'
    elif isinstance(data, list):
        return "[" + ", ".join(json_encode(d) for d in data) + "]"
    elif isinstance(data,dict):
	return data
#	result={}
#	for d in data:
#		print "looo"
#		return dictt(d,data,result)
#		print "ttttt"
#	print "mpppp"
		
    else:
        raise TypeError("%s is not JSON serializable" % repr(data))

def escape_string(s):
    """Escapes double-quote, tab and new line characters in a string."""
    s = s.replace('"', '\\"')
    s = s.replace("\t", "\\t")
    s = s.replace("\n", "\\n")
    return s
#def dictt(a,data,result):
	
#	print "suuuu"
#	result[a]=data[a]
#	return result
	
print json_encode({'q':2,'6':{'d':4}})
