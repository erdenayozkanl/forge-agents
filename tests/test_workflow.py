from agents.workflow import Workflow

def test_bounded_workflow_writes_trace(tmp_path, monkeypatch):
    import agents.workflow as w
    monkeypatch.setattr(w,'BASE',tmp_path)
    result=Workflow(llm=False).run('How is retrieval evaluated?')
    assert len(result['trace'])==4
    assert result['verification']['citation_numbers_valid']
    assert (tmp_path/'runs'/f"{result['run_id']}.json").exists()

def test_rejects_blank_task():
    import pytest
    with pytest.raises(ValueError):
        Workflow().run(' ')
