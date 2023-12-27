from query_quiver.prompt import PROMPTS


def test_prompt():
    for _, prompt in PROMPTS.items():
        assert prompt["idea_generate_system_prompt"]
        assert prompt["idea_generate_user_prompt"]
