import sys

statements = []


def count_clucks(tokens):
    return sum(1 for t in tokens if t == "cluck")

def execute(statements, variables):
    for stmt in statements:
        kind = stmt[0]

        if kind == "nest":
            name = stmt[1]
            variables[name] = 0

        elif kind == "feed":
            name = stmt[1]
            value = stmt[2]
            variables[name] = value

        elif kind == "bok":
            name = stmt[1]
            variables[name] += 1

        elif kind == "peck":
            name = stmt[1]
            variables[name] -= 1

        elif kind == "cluck":
            name = stmt[1]
            print(variables[name])

        elif kind == "loop":
            name = stmt[1]
            body = stmt[2]
            while variables[name] != 0:
                execute(body, variables)

if (len(sys.argv) < 2):
    print("Error: python chicken <filename>")
    sys.exit(0)

filename = sys.argv[1]

with open(filename, "r") as file:
    lines = file.readlines()

i = 0
while i < len(lines):
    line = lines[i].strip()

    if not line:
        i += 1
        continue

    tokens = line.split()
    cmd = tokens[0]

    if cmd == "coop":
        name = tokens[1]
        body = []
        i += 1

        while i < len(lines) and lines[i].strip() != "roost":
            inner_line = lines[i].strip()

            if not inner_line:
                i += 1
                continue

            inner_tokens = inner_line.split()
            inner_cmd = inner_tokens[0]

            if inner_cmd == "bok":
                body.append(("bok", inner_tokens[1]))
            elif inner_cmd == "peck":
                body.append(("peck", inner_tokens[1]))
            elif inner_cmd == "cluck":
                body.append(("cluck", inner_tokens[1]))
            else:
                print(f"Unknown command in loop: {inner_line}")

            i += 1

        statements.append(("loop", name, body))

    elif cmd == "nest":
        statements.append(("nest", tokens[1]))

    elif cmd == "feed":
        name = tokens[1]
        value = count_clucks(tokens[2:])
        statements.append(("feed", name, value))

    elif cmd == "bok":
        statements.append(("bok", tokens[1]))

    elif cmd == "peck":
        statements.append(("peck", tokens[1]))

    elif cmd == "cluck":
        statements.append(("cluck", tokens[1]))

    else:
        print(f"Unknown command: {line}")

    i += 1

    # print(statements) # <-- DEBUG STATEMENT

    variables = {}
    execute(statements, variables)