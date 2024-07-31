import numpy as np
def input_matrix(n, name):
    print(f"Enter the elements of the {name} matrix row by row (total {n*n} elements):")
    elements = []
    for _ in range(n):
        row = list(map(float, input().split()))
        if len(row) != n:
            raise ValueError(f"Each row must have exactly {n} elements.")
        elements.append(row)
    return np.array(elements)


def calculate_sigma_xz(L, phi):
    n = L.shape[0]
    I = np.identity(n)
    I_minus_L = I - L
    I_minus_L_invT = np.linalg.inv(I_minus_L).T
    Sigma_XZ = I_minus_L_invT @ phi @ I_minus_L
    return Sigma_XZ


def main():
    n = int(input("Enter the dimension of the square matrices: "))
    
    
    L = input_matrix(n, "lower triangular (L)")
    phi = input_matrix(n, "phi")
    
   
    if not np.allclose(L, np.tril(L)):
        raise ValueError("Matrix L must be lower triangular.")
    
   
    Sigma_XZ = calculate_sigma_xz(L, phi)
    
    
    print("The resultant matrix Sigma_XZ is:")
    print(Sigma_XZ)
    rank = np.linalg.matrix_rank(Sigma_XZ)
    print(f"The rank of the resultant matrix Sigma_XZ is: {rank}")

if __name__ == "__main__":
    main()
