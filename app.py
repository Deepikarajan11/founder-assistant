import gradio as gr
import random

# Wrap your route_input() inside a Gradio-friendly function
def gradio_chat(user_input):
    return route_input(user_input)

def get_daily_affirmation():
    affirmations = [
        "You are capable of amazing things.",
        "Every step you take matters.",
        "Your work is meaningful and impactful.",
        "You bring empathy and intelligence into everything you build.",
        "You’ve got this, Bizz."
    ]
    return random.choice(affirmations)

# Launch Gradio interface
with gr.Blocks() as demo:
    gr.Markdown("## 💼 Entrepreneur Assistant Chatbot")

    with gr.Row():
        affirm_btn = gr.Button("🌞 Daily Affirmation")
        affirm_output = gr.Textbox(label="Affirmation")

    affirm_btn.click(fn=get_daily_affirmation, outputs=affirm_output)

    with gr.Row():
        user_input = gr.Textbox(label="Your Message", placeholder="Ask about goals, reminders, pitch, dashboard...")
        output = gr.Textbox(label="Assistant Response", lines=10)

    send_btn = gr.Button("Send")
    send_btn.click(fn=gradio_chat, inputs=user_input, outputs=output)

    with gr.Row():
        affirm_btn = gr.Button("🌞 Daily Affirmation")
        affirm_output = gr.Textbox(label="Affirmation")
        affirm_btn.click(fn=get_daily_affirmation, outputs=affirm_output)

    with gr.Row():
        dashboard_btn = gr.Button("📊 Show Dashboard")
        dashboard_output = gr.Textbox(label="Dashboard Summary", lines=6)
        dashboard_btn.click(fn=lambda: generate_dashboard(load_memory()), outputs=dashboard_output)

    with gr.Row():
        calendar_btn = gr.Button("📅 What's Today?")
        calendar_output = gr.Textbox(label="Calendar Info")
        calendar_btn.click(fn=lambda: handle_calendar_request("today"), outputs=calendar_output)

demo.launch()
