


# import matplotlib.pyplot as plt

# def plot_toolpath_with_heat(layers):
#     fig, ax = plt.subplots()
#     ax.set_title("Toolpath with Heat Overlay")
#     ax.set_xlabel("X")
#     ax.set_ylabel("Y")

#     for z, polyline in layers.items():
#         if not polyline:
#             continue

#         xs, ys = zip(*polyline)
#         ax.plot(xs, ys, label=f"Layer {z}", alpha=0.6)

#         # Simple heat spot overlay (red circle)
#         for x, y in polyline:
#             heat = plt.Circle((x, y), 0.1, color='red', alpha=0.1)
#             ax.add_patch(heat)

#     ax.legend()
#     ax.set_aspect("equal")
#     return fig




# import plotly.graph_objects as go
# import numpy as np

# def gaussian(x, y, x0, y0, sigma=0.05):
#     return np.exp(-((x - x0)**2 + (y - y0)**2) / (2 * sigma**2))

# def plot_3d_toolpath_with_heat(layers, selected_layer=None, show_heat=True):
#     fig = go.Figure()

#     for z, polyline in layers.items():
#         if selected_layer is not None and z != selected_layer:
#             continue
#         if not polyline:
#             continue

#         xs, ys = zip(*polyline)
#         zs = [z] * len(xs)

#         fig.add_trace(go.Scatter3d(
#             x=xs, y=ys, z=zs,
#             mode='lines+markers',
#             line=dict(width=4),
#             marker=dict(size=3),
#             name=f"Layer {z}"
#         ))

#         if show_heat:
#             for x, y in polyline:
#                 gx, gy = np.meshgrid(
#                     np.linspace(x-0.1, x+0.1, 10),
#                     np.linspace(y-0.1, y+0.1, 10)
#                 )
#                 gz = gaussian(gx, gy, x, y)
#                 fig.add_trace(go.Surface(
#                     x=gx, y=gy, z=np.full_like(gz, z),
#                     surfacecolor=gz,
#                     colorscale='Reds',
#                     opacity=0.4,
#                     showscale=False
#                 ))

#     fig.update_layout(
#         title="3D Tool Path with Heat Overlay",
#         scene=dict(
#             xaxis_title='X',
#             yaxis_title='Y',
#             zaxis_title='Layer (Z)',
#             aspectmode='data'
#         )
#     )
#     return fig





# import plotly.graph_objects as go
# import numpy as np

# def gaussian(x, y, x0, y0, sigma=0.05):
#     return np.exp(-((x - x0)**2 + (y - y0)**2) / (2 * sigma**2))

# def plot_3d_toolpath_with_heat(layers, selected_layer=None, show_heat=True):
#     fig = go.Figure()

#     for z, polyline in layers.items():
#         if selected_layer is not None and z != selected_layer:
#             continue
#         if not polyline:
#             continue

#         xs, ys = zip(*polyline)
#         zs = [z] * len(xs)

#         fig.add_trace(go.Scatter3d(
#             x=xs, y=ys, z=zs,
#             mode='lines+markers',
#             line=dict(width=4),
#             marker=dict(size=3),
#             name=f"Layer {z}"
#         ))

#         if show_heat:
#             # Sample every 5th point only
#             for i, (x, y) in enumerate(polyline):
#                 if i % 5 != 0:
#                     continue
#                 gx, gy = np.meshgrid(
#                     np.linspace(x - 0.05, x + 0.05, 5),
#                     np.linspace(y - 0.05, y + 0.05, 5)
#                 )
#                 gz = gaussian(gx, gy, x, y)
#                 fig.add_trace(go.Surface(
#                     x=gx, y=gy, z=np.full_like(gz, z),
#                     surfacecolor=gz,
#                     colorscale='Reds',
#                     opacity=0.3,
#                     showscale=False
#                 ))

#     fig.update_layout(
#         title="3D Tool Path with Optimized Heat Overlay",
#         scene=dict(
#             xaxis_title='X',
#             yaxis_title='Y',
#             zaxis_title='Layer (Z)',
#             aspectmode='data'
#         ),
#         margin=dict(l=0, r=0, t=30, b=0)
#     )
#     return fig




def plot_3d_toolpath_with_heat(layers, selected_layer=None, show_heat=True, max_heat_points=50):
    import plotly.graph_objects as go
    import numpy as np

    def gaussian(x, y, x0, y0, sigma=0.05):
        return np.exp(-((x - x0)**2 + (y - y0)**2) / (2 * sigma**2))

    fig = go.Figure()
    heat_count = 0

    for z, polyline in layers.items():
        if selected_layer is not None and z != selected_layer:
            continue
        if not polyline:
            continue

        xs, ys = zip(*polyline)
        zs = [z] * len(xs)

        fig.add_trace(go.Scatter3d(
            x=xs, y=ys, z=zs,
            mode='lines+markers',
            line=dict(width=3),
            marker=dict(size=2),
            name=f"Layer {z}"
        ))

        if show_heat:
            for i, (x, y) in enumerate(polyline):
                if heat_count >= max_heat_points:
                    break
                if i % 5 != 0:
                    continue
                gx, gy = np.meshgrid(
                    np.linspace(x - 0.05, x + 0.05, 5),
                    np.linspace(y - 0.05, y + 0.05, 5)
                )
                gz = gaussian(gx, gy, x, y)
                fig.add_trace(go.Surface(
                    x=gx, y=gy, z=np.full_like(gz, z),
                    surfacecolor=gz,
                    colorscale='Reds',
                    opacity=0.3,
                    showscale=False
                ))
                heat_count += 1

    fig.update_layout(
        title="3D Tool Path with Gaussian Heat",
        scene=dict(xaxis_title='X', yaxis_title='Y', zaxis_title='Z', aspectmode='data'),
        margin=dict(l=0, r=0, t=30, b=0),
    )
    return fig
