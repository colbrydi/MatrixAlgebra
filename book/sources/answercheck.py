import hashlib
import numpy as np
import sympy as sym
import sys
import textwrap


# detailedwarnings = True

# Things I fixed. Fixed Matrix rounding error
# Added more print warnings

# TODO: Fix Printwarnings


def printwarning(message):
    if checkanswer.detailedwarnings:
        print(message)


class checkanswer():
    detailedwarnings = True

    def __init__(self, var, hashtag=None):
        checkanswer.basic(var, hashtag)

    def basic(var, hashtag=None):
        """Fuanction that encodes answers in a string called a Hash.
        This is a one way function so a correct answer will generate the
        correct has. An incorrect answer will generate an incorrect hash."""

        if checkanswer.detailedwarnings:
            print(f"Testing {var}")
        else:
            print(f"Testing Answer")
            
        curr_printopts = np.get_printoptions()
        np.set_printoptions(threshold=sys.maxsize)
        varstr = f"{var}"
        np.set_printoptions(threshold=curr_printopts['threshold'])

        t2 = varstr.encode("utf-8")
        m = hashlib.md5(t2)
        checktag = m.hexdigest()
        if hashtag:
            if checktag == hashtag:
                print("Answer seems to be correct\n")
            else:
                print("Answer seems to be incorrect\n")
                assert checktag == hashtag, f"Answer is incorrect {checktag}"
        else:
            raise TypeError(f"No answer hastag provided: {checktag}")

    def float(A, hashtag=None, decimal_accuracy = 5):
        """Function to check matrix type before hashing."""
        if(type(A) is not float):
            if(type(A) is list):
                printwarning(textwrap.dedent(f"""
                CheckWarning: passed variable is a list and not a float...
                    Cannot convert list to float directly. We will assume this
                    list has only one element and covert to a numpy matrix
                    using ```A = np.matrix(A)```.\n"""))
                A = np.matrix(A)
            printwarning(textwrap.dedent(f"""
            CheckWarning: passed variable is {type(A)} and not a float.
                Trying to convert to a float using ```A = float(A)```.\n"""))
            A = float(A)
        A = np.round(A, decimals=decimal_accuracy)
        if A == -0.00:
            printwarning(textwrap.dedent(f"""
            CheckWarning: Value is negative zero...
                Converting to positive zero before checking using ```A = 0.00```.\n"""))
            A = 0.00
        return checkanswer.basic(A, hashtag)

    def make_vector(A, decimal_accuracy = 5):
        """Function to check matrix type before hashing."""
        if(type(A) is not np.matrix):
            printwarning(textwrap.dedent(f"""
            CheckWarning: passed variable is {type(A)} and not a numpy.matrix.
                Trying to convert to a array matrix using ```A = np.matrix(A)```.\n"""))
            A = np.matrix(A)
        if not np.issubdtype(A.dtype, np.dtype(float).type):
            printwarning(textwrap.dedent(f"""
            CheckWarning: passed matrix is {A.dtype} and not {np.dtype(float).type}...
                Trying to convert to float using ```A = A.astype(float)```.\n"""))
            A = A.astype(float)
        if(A.shape[0] != 1 and A.shape[1] != 1):
            assert A.shape[0] != 1 and A.shape[1] != 1, \
                f"Matrix is not of vector format {A}"
        if(A.shape[0] != 1):
            printwarning(textwrap.dedent(f"""
            CheckWarning: numpy.matrix is row vector...
                Trying to convert to a column vector using ```A = A.T```.\n"""))
            A = A.T
        A = np.round(A, decimals=decimal_accuracy)
        if not A[A == -0].size == 0:
            printwarning(textwrap.dedent(f"""
            CheckWarning: Vector contains negative values for zero...
                Converting to positive values of zero using  ```A[A==-0] = 0```.\n"""))
            A[A == -0] = 0.00
        return A
    
    def vector(A, hashtag=None, decimal_accuracy = 5):
        A = checkanswer.make_vector(A, decimal_accuracy)
        return checkanswer.basic(A, hashtag)
    
    def eq_vector(A, hashtag=None, decimal_accuracy = 5):
        A = checkanswer.make_vector(A, decimal_accuracy)
        vecsum = np.sqrt(np.sum(np.dot(A,A.T)))
        if not vecsum == 1:
            printwarning(textwrap.dedent(f"""
            CheckWarning: Vector sum of {A} has total value of {vecsum}...
                Trying to normalize to unit vector to check answer using
                using ```A = A/{vecsum}```.\n\n"""))
            A = A/vecsum
        if(A[0, 0] < 0):
            printwarning(textwrap.dedent(f"""
            CheckWarning: First element of {A} is negative ({A[0,0]}.
                Trying to normalize by making this value positive using ```A = -A```.\n"""))
            A = -A
        A = np.round(A, decimals=decimal_accuracy)
        if not A[A == -0].size == 0:
            printwarning(textwrap.dedent(f"""
            CheckWarning: Vector contains negative values for zero...
            Converting to positive values of zero using  ```A[A==-0] = 0```.\n"""))
        A[A == -0] = 0.00
        return checkanswer.basic(A, hashtag)

    def make_matrix(A, decimal_accuracy = 5):
        if(type(A) is not np.matrix):
            printwarning(textwrap.dedent(f"""
            CheckWarning: passed variable is {type(A)} and not a numpy.matrix...
                Trying to convert to a array matrix using ```A = np.matrix(A)```.\n"""))
            A = np.matrix(A)
        if not np.issubdtype(A.dtype, np.dtype(float).type):
            printwarning(textwrap.dedent(f"""
            CheckWarning: passed matrix is {A.dtype} and not {np.dtype(float).type}...
                Trying to convert to float using ```A = A.astype(float)```.\n"""))
            A = A.astype(float)
        A = np.round(A, decimals=decimal_accuracy)
        if not A[A == -0].size == 0:
            printwarning(textwrap.dedent(f"""
            CheckWarning: Matrix contains negative values for zero...
                Converting to positive values of zero using  ```A[A==-0] = 0```.\n"""))
            A[A == -0] = 0.00
        return A
    
    def matrix(A, hashtag=None, decimal_accuracy = 5):
        """Function to check matrix type before hashing."""
        A = checkanswer.make_matrix(A, decimal_accuracy)
        return checkanswer.basic(A, hashtag)

    # TODO: Not complete or tested.
    def eq_matrix(A, hashtag=None, decimal_accuracy = 5):
        """Function to convert matrix to reduced row echelon form
        and then run hashing."""
        A = checkanswer.make_matrix(A, decimal_accuracy)
        symA = sym.Matrix(A)
        symA = symA.rref()[0]
        A = np.matrix(symA)
        A = checkanswer.make_matrix(A)
        return checkanswer.basic(A, hashtag)
