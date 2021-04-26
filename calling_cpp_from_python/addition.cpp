#ifdef __cplusplus
extern "C" float c_addition(float float_1, float float_2)
{
    float return_value = float_1 + float_2;

    return return_value;
}

#else
{
    std::cout << "Running in C++!";
}
#endif
