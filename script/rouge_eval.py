from pyrouge import Rouge155

r = Rouge155()
r.system_dir = '../test_files/'#'path/to/system_summaries'
r.model_dir = '../output/'
r.system_filename_pattern = 'test.eval_articles.txt'
r.model_filename_pattern = 'eval_articles.1_300000.txt'

output = r.convert_and_evaluate()
print(output)
output_dict = r.output_to_dict(output)