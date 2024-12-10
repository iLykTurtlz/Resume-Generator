const Slider = ({ label, min, max, value, step, onChange }) => {
  return (
    <div className="flex flex-col items-start mb-6">
      <label className="mb-2 text-sm font-bold text-gray-200">{label}</label>
      <input
        type="range"
        min={min}
        max={max}
        value={value}
        step={step}
        onChange={onChange}
        className="w-full"
      />
      <div className="text-sm text-gray-300 mt-1">Value: {value}</div>
    </div>
  );
};
