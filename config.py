
folder_path = {
    "train_dataset" : "dataset/Total_Train_dataset/",
    "test_dataset" : "dataset/Total_Test_dataset/",
    "inference_image" : "model_d_infer/images/"
}

file_path = {
    "train_xlsx" : "model_d_infer/Train_model_d.xlsx",
    "test_xlsx" : "model_d_infer/Test_model_d.xlsx"
}

hyperparameter_train = {
    "training_iters" : 10,
    "learning_rate" : 0.001,
    "batch_size" : 1,
    "no_epochs" : 500,
    "n_classes" : 3
}

model_ckpts = {
    "saved_model" : "model_d_infer/agp_birads_model_d.ckpt",
    "model_output" : "model_d_infer/output"
}
