from client import InteractiveCanvasArtifactSandboxRendererClient

def main():
    client = InteractiveCanvasArtifactSandboxRendererClient()
    res = client.render_isolated_artifact_canvas('INTERACTIVE_SVG_SIMULATOR', 'Gravitational n-body orbital simulation')
    print('Canvas Session: ' + res['canvas_session_id'] + ' (' + res['artifact_type'] + ')')
    print('Render Latency: ' + str(res['dom_render_latency_ms']) + 'ms (Isolated: ' + str(res['iframe_sandbox_isolated']) + ')')
    print('Sandbox URL: ' + res['sandbox_view_url'] + ' | Export Ready: ' + str(res['standalone_html_export_ready']))

if __name__ == '__main__':
    main()
