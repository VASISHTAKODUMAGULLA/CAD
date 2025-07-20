# def parse_cli(file_path):
#     layers = {}
#     current_layer = None
#     current_polyline = []

#     with open(file_path, 'r') as f:
#         for line in f:
#             line = line.strip()
#             if line.startswith("$$LAYER"):
#                 if current_layer is not None and current_polyline:
#                     layers[current_layer] = current_polyline
#                 current_layer = float(line.split("/")[1])
#                 current_polyline = []
#             elif line.startswith("$$"):
#                 continue
#             else:
#                 try:
#                     x, y = map(float, line.split())
#                     current_polyline.append((x, y))
#                 except:
#                     continue
#         if current_layer and current_polyline:
#             layers[current_layer] = current_polyline
#     return layers




# import re

# def parse_cli(file_path):
#     layers = {}
#     current_layer = None

#     with open(file_path, "r") as f:
#         for line in f:
#             line = line.strip()

#             if line.startswith("$$LAYER/"):
#                 current_layer = float(line.split("/")[1])
#                 layers[current_layer] = []

#             elif line.startswith("$$HATCHES"):
#                 # Extract coordinates after comma(s)
#                 coords = list(map(int, re.findall(r"-?\d+", line)))
#                 # Skip the first 2 numbers (e.g., "1,37")
#                 coords = coords[2:]

#                 # Group into (x, y) pairs and normalize scale
#                 points = [(x / 1000, y / 1000) for x, y in zip(coords[::2], coords[1::2])]
#                 layers[current_layer].extend(points)

#     return layers



import re

def parse_cli(file_path):
    layers = {}
    current_layer = None

    with open(file_path, "r") as f:
        for line in f:
            line = line.strip()

            if line.startswith("$$LAYER/"):
                current_layer = float(line.split("/")[1])
                layers[current_layer] = []

            elif line.startswith("$$HATCHES"):
                coords = list(map(int, re.findall(r"-?\d+", line)))
                if len(coords) <= 2:
                    continue  # no points
                coords = coords[2:]  # skip header values
                points = [(x / 1000, y / 1000) for x, y in zip(coords[::2], coords[1::2])]
                layers[current_layer].extend(points)

    return layers
