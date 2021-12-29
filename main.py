def make_lookups(grid, fn='sanat.txt'):
    # Make set of valid characters.
    chars = set()
    for word in grid:
        chars.update(word)

    words = set(x.strip() for x in open(fn, encoding="utf-8") if set(x.strip()) <= chars)
    prefixes = set()
    for w in words:
        for i in range(len(w)+1):
            prefixes.add(w[:i])

    #print(prefixes)
    return words, prefixes

def make_graph(grid):
    root = None
    graph = { root:set() }
    chardict = { root:'' }

    for i, row in enumerate(grid):
        for j, char in enumerate(row):
            chardict[(i, j)] = char
            node = (i, j)
            children = set()
            graph[node] = children
            graph[root].add(node)
            add_children(node, children, grid)

    return graph, chardict

def add_children(node, children, grid):
    x0, y0 = node
    for i in [-1,0,1]:
        x = x0 + i
        if not (0 <= x < len(grid)):
            continue
        for j in [-1,0,1]:
            y = y0 + j
            if not (0 <= y < len(grid[0])) or (i == j == 0):
                continue

            children.add((x,y))

def to_word(chardict, pos_list):
    return ''.join(chardict[x] for x in pos_list)

def find_words(graph, chardict, position, prefix, results, words, prefixes):
    """ Arguments:
      graph :: mapping (x,y) to set of reachable positions
      chardict :: mapping (x,y) to character
      position :: current position (x,y) -- equals prefix[-1]
      prefix :: list of positions in current string
      results :: set of words found
      words :: set of valid words in the dictionary
      prefixes :: set of valid words or prefixes thereof
    """
    word = to_word(chardict, prefix)

    if word not in prefixes:
        return

    if word in words:
        results.add(word)

    for child in graph[position]:
        if child not in prefix:
            find_words(graph, chardict, child, prefix+[child], results, words, prefixes)




if __name__ == '__main__':
    while(True):
        letters = input("Input the letters: ").lower()

        if letters == "exit":
            exit()
        grid = [letters[0:4], letters[4:8], letters[8:12], letters[12:16]]

        g, c = make_graph(grid)
        w, p = make_lookups(grid)
        res = set()
        find_words(g, c, None, [], res, w, p)
        results = list(res)
        results.sort(key=len)

        temp = []
        for word in results:
            if len(word) < 3 or len(word) > 10:
                continue
            else:
                temp.append(word)

        for word in temp:
            print(word)