from easydict import EasyDict as edict
api_graph = edict()
api_graph= api_graph

api_graph.no_tasks = 10
api_graph.mem_size = 2000 # 2000
api_graph.mem_size_semi_supervised = 2000 #2000
api_graph.replay_size = 1500
api_graph.n_epochs = 5
api_graph.minority_allocation = 0.8
api_graph.batch_size = 64
api_graph.learning_rate = 1e-4#0.001
api_graph.label = 'api_graph'
api_graph.enable_checkpoint = False
api_graph.taskaware_ecbrs = False
api_graph.train_data_lstm = 0.5
api_graph.num_mini_tasks = 200
api_graph.lstm_epochs = 3
api_graph.interim_model_epochs = 1
api_graph.lstm_hidden_size = 10
api_graph.param_weights_queue_length = 50
api_graph.pattern_per_exp = 50
api_graph.is_lazy_training = True
api_graph.clstrategy = None
api_graph.store_weights = False
api_graph.train_lstm = True
api_graph.store_grads = False
api_graph.image_resolution = None
api_graph.bool_encode_anomaly=False
api_graph.bool_encode_benign=False
api_graph.load_whole_train_data=False