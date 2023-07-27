class Controller:
    @classmethod
    def control(
        self,
        memory,
        config,
        current_objective,
        executor_response,
        tool_response,
        evaluator_response,
    ):
        current_state = {
            "executor": executor_response,
            "tool": tool_response,
            "evaluator": evaluator_response,
        }

        memory.states.append(current_state)

        if evaluator_response["is_valid"]:
            config.repo.git.add(A=True)
            config.repo.index.commit(current_objective["title"])

            branch = config.repo.head.reference
            last_commit = branch.commit.parents[0]
            diff = last_commit.diff()

            memory.commited_files = [file.a_path for file in diff]

        else:
            last_commit = config.repo.head.commit
            config.repo.git.reset("--hard", last_commit)

            memory.errors += 1
