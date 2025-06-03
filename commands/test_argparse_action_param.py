import argparse


def list_help_n_exit():
  scrmsg = f"test list_help_n_exit"
  print(scrmsg)


def function_a(args):
    print("Executing function A with:", args.param_a)


def function_b(args):
    print("Executing function B with:", args.param_b)


def process():
  parser = argparse.ArgumentParser(description="Example program")
  parser.add_argument("command", choices=["a", "b"],
                      help="Choose a command")
  parser.add_argument("--param_a",
                      help="Parameter for function A")
  parser.add_argument("--param_b",
                      help="Parameter for function B")
  args = parser.parse_args()

  function_mapping = {
    "a": function_a,
    "b": function_b,
  }

  selected_function = function_mapping.get(args.command)
  if selected_function:
      selected_function(args)
  else:
      print("Invalid command")


def adhoc_test():
  """
  Example for an adhoc test:
    --rootdir="/home/dados/VideoAudio/Soc vi/Law vi/BRA Dir vi/Sab Dir vi/completed Sab Dir ytvi"
  """
  pass


if __name__ == '__main__':
  """
  """
  process()
  adhoc_test()
