# output all supersets for a set of items
# Ex {1,2,3} = {}, {1}, {2}, {3}, {1,2}, {1,3}, {2,3}, {1,2,3}

# empty
a = []
# >> {}

# 1 item
a = [1]
# >> {}, {1}

# 2 items
a = [1, 2]
# >> {}, {1}, {2}, {1,2}

def super_set(a, s:[]):
    if len(a) == 0:
        return []
    elif len(a) == 1:
        return [a[0]]
    for i in a:
        b = set(a).remove(i)
        super_set(b, ))
#    else:
#        return a
#

"""
list * subsets(string s, list * v) {

    if(s.length() == 1) {
        list.add(s);    
        return v;
    }
    else
    {
        list * temp = subsets(s[1 to length-1], v);
        int length = temp->size();

        for(int i=0;i<length;i++) {
            temp.add(s[0]+temp[i]);
        }

        list.add(s[0]);
        return temp;
    }
}
"""