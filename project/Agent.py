from tensorflow.keras.layers import Dense
from tensorflow.keras.models import Sequential

class Agent:
    def __init__(self, grid_size):
        self.grid_size = grid_size
        self.model = self.build_model()

    def build_model(self):
        # Create a sequential model with 3 layers
        model = Sequential([
            # Input layer expects a flattened grid, hence the input shape is grid_size squared
            Dense(128, activation='relu', input_shape=(self.grid_size**2,)),
            Dense(64, activation='relu'),
            # Output layer with 4 units for the possible actions (up, down, left, right)
            Dense(4, activation='linear')
        ])

        model.compile(optimizer='adam', loss='mse')

        return model
