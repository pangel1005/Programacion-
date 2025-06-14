import argparse
from task_manager import tasks


def main():
    parser = argparse.ArgumentParser(description="Simple Task Manager")
    subparsers = parser.add_subparsers(dest='command')

    add_parser = subparsers.add_parser('add', help='Add a new task')
    add_parser.add_argument('description', help='Task description')

    subparsers.add_parser('list', help='List tasks')

    done_parser = subparsers.add_parser('done', help='Mark task as done')
    done_parser.add_argument('index', type=int, help='Task number (1-based)')

    args = parser.parse_args()

    if args.command == 'add':
        tasks.add_task(args.description)
        print("Task added.")
    elif args.command == 'list':
        tasks.list_tasks()
    elif args.command == 'done':
        tasks.mark_done(args.index - 1)
        print("Task marked as done.")
    else:
        parser.print_help()


if __name__ == '__main__':
    main()
