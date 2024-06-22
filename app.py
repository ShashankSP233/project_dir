import streamlit as st
import time
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from streamlit_option_menu import option_menu

#=====================================================================================================================

st.set_page_config(page_title="JAVIS")
st.markdown("<h3 style='text-align: justify; color: #faca2b; font-weight: bold;'>Prim's Algorithm: Utilizing Prim's algorithm to discover a Minimum Spanning Tree (MST) within a graph</h3>", unsafe_allow_html=True)
st.write("---")


#=====================================================================================================================

def show_developer():
    st.sidebar.write("---")
    st.sidebar.markdown("""<p style="color: #faca2b; font-weight: bold; font-size: 24px;">Developer</p>""", unsafe_allow_html=True)
    st.sidebar.markdown("""<ul>
                        <li>Rudra Pratap Singh      - 07</li>
                        <li>Shashank Singh Parihar  - 08</li>
                        <li>Shashank Singh          - 09</li>
                        </ul>""", unsafe_allow_html=True)
    st.sidebar.write("Mentor : Mr. Aniket Dev")
    
def show_settings():
    st.sidebar.write("---")
    st.sidebar.markdown("""<p style="color: #faca2b; font-weight: bold; font-size: 24px;">Settings</p>""", unsafe_allow_html=True)
    st.sidebar.checkbox("Enable Notifications", value=True)
    st.sidebar.checkbox("Chat history & training", value=True)
            
with st.sidebar:
    selected = option_menu("Main Menu",["Developer", "Settings"],
                                icons=["people-fill", "gear"],menu_icon="cast", default_index=0)
if selected == "Developer":
    show_developer()
elif selected == "Settings":
    show_settings()

#=====================================================================================================================

if "messages" not in st.session_state.keys():
    st.session_state.messages = [{"role": "assistant", "content": "Hello, Aniket Sir, it's Javis. How are you? I am your virtual assistant. Today, my team, comprising Rudra Pratap Singh, Shashank Parihar Singh, Shashank Singh, and I, are excited to showcase our utilization of Prim's Algorithm to construct a Minimum Spanning Tree (MST)."}]
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

#time.sleep(10)

#=====================================================================================================================

st.set_option('deprecation.showPyplotGlobalUse', False)
def generate_graph(num_vertices, weights):
    G = nx.Graph()
    for weight in weights:
        v1, v2, w = weight
        G.add_edge(v1, v2, weight=w)
    return G

def visualize_graph(graph):
    fig, ax = plt.subplots(facecolor='#0e1117')
    node_color = "#faca2b"
    edge_color = "white"
    pos = nx.spring_layout(graph)
    nx.draw(graph, pos, with_labels=True, node_size=700, node_color=node_color,
            font_size=12, font_weight="bold", edge_color=edge_color)
    labels = nx.get_edge_attributes(graph, "weight")
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=labels)
    ax.set_facecolor('#0e1117')  # Setting the background color of the axis
    ax.axis('off')
    fig.set_facecolor('#0e1117')  # Setting the background color of the figure
    st.pyplot(fig)
    
#=====================================================================================================================

def main():
    rate = -1
    num_vertices = st.number_input("Enter the number of vertices:", min_value=2, step=1)
    
    weights = []
    for i in range(num_vertices):
        for j in range(i+1, num_vertices):
            weight = st.number_input(f"Weight from vertex {i} to {j}:", step=1, value=0)
            weights.append((i, j, weight))
    
    if st.button("Generate Graph"):
        graph = generate_graph(num_vertices, weights)
        st.write("Original Graph:")
        visualize_graph(graph)
        
        # Prim's Algorithm to find MST
        mst = prim_mst(graph)
        
        st.write("Minimum Spanning Tree (MST):")
        visualize_graph(mst)
    
        st.write(f"Time Complexity : O(V^2) = O({num_vertices}^2) = {num_vertices**2}")
        st.write(f"Space Complexity : O(V^2) = O({num_vertices}^2) = {num_vertices**2}")
        
        if "messages"  in st.session_state.keys():
            st.session_state.messages = [{"role": "assistant", "content": "Thank you for your time!"}]
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.write(message["content"])

#=====================================================================================================================

def prim_mst(graph):
    mst = nx.Graph()
    start_node = list(graph.nodes())[0]
    visited = set([start_node])
    
    while len(visited) < len(graph.nodes()):
        min_weight = float('inf')
        min_edge = None
        
        for node in visited:
            for neighbor, edge_data in graph.adj[node].items():
                if neighbor not in visited and edge_data['weight'] < min_weight:
                    min_weight = edge_data['weight']
                    min_edge = (node, neighbor)
        
        if min_edge is not None:
            mst.add_edge(min_edge[0], min_edge[1], weight=min_weight)
            visited.add(min_edge[1])
    
    return mst
#=====================================================================================================================

if __name__ == "__main__":
    main()
