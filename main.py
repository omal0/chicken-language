import sys

statements = []


def count_clucks(tokens):
    return sum(1 for t in tokens if t == "cluck")


def execute(statements, state):
    tape = state["tape"]
    labels = state["labels"]

    for stmt in statements:
        kind = stmt[0]

        if kind == "nest":
            name = stmt[1]
            labels[name] = state["pointer"]

        elif kind == "roam":
            name = stmt[1]
            state["pointer"] = labels[name]

        elif kind == "feed":
            value = stmt[1]
            tape[state["pointer"]] = value

        elif kind == "bok":
            tape[state["pointer"]] += 1

        elif kind == "peck":
            tape[state["pointer"]] -= 1

        elif kind == "strut":
            state["pointer"] += 1

        elif kind == "shuffle":
            state["pointer"] -= 1

        elif kind == "cluck":
            print(tape[state["pointer"]])

        elif kind == "loop":
            body = stmt[1]
            while tape[state["pointer"]] != 0:
                execute(body, state)

def parse_block(lines, i=0, inside_loop=False):
    statements = []

    while i < len(lines):
        line = lines[i]
        line = line.split("#")[0].strip()

        if not line:
            i += 1
            continue

        tokens = line.split()
        cmd = tokens[0]

        if cmd == "roost":
            if inside_loop:
                return statements, i + 1
            else:
                print("Error: roost without coop")
                sys.exit(1)

        elif cmd == "coop":
            body, i = parse_block(lines, i + 1, inside_loop=True)
            statements.append(("loop", body))

        elif cmd == "nest":
            statements.append(("nest", tokens[1]))
            i += 1

        elif cmd == "roam":
            statements.append(("roam", tokens[1]))
            i += 1

        elif cmd == "feed":
            value = count_clucks(tokens[1:])
            statements.append(("feed", value))
            i += 1

        elif cmd == "bok":
            statements.append(("bok",))
            i += 1

        elif cmd == "peck":
            statements.append(("peck",))
            i += 1

        elif cmd == "strut":
            statements.append(("strut",))
            i += 1

        elif cmd == "shuffle":
            statements.append(("shuffle",))
            i += 1

        elif cmd == "cluck":
            statements.append(("cluck",))
            i += 1

        else:
            print(f"Unknown command: {line}")
            sys.exit(1)

    if inside_loop:
        print("Error: missing roost")
        sys.exit(1)

    return statements, i

if len(sys.argv) < 2:
    print("Error: python main.py <filename>")
    sys.exit(1)

filename = sys.argv[1]

with open(filename, "r") as file:
    lines = file.readlines()

statements, _ = parse_block(lines)

state = {
    "tape": [0] * 30000,
    "pointer": 0,
    "labels": {}
}

execute(statements, state)