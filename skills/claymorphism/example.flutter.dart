import 'package:flutter/material.dart';

class ClayCard extends StatelessWidget {
  const ClayCard({super.key, this.onPressed});

  final VoidCallback? onPressed;

  @override
  Widget build(BuildContext context) {
    return LayoutBuilder(
      builder: (context, constraints) {
        final compact = constraints.maxWidth < 600;
        final padding = compact ? 16.0 : 24.0;
        final radius = compact ? 24.0 : 32.0;

        return DecoratedBox(
          decoration: const BoxDecoration(color: Color(0xFFF4F1FB)),
          child: Center(
            child: Container(
              constraints: const BoxConstraints(maxWidth: 560),
              padding: EdgeInsets.all(padding),
              decoration: BoxDecoration(
                color: const Color(0xFFCFD4FF),
                borderRadius: BorderRadius.circular(radius),
                boxShadow: [
                  BoxShadow(
                    color: const Color(0x52504196),
                    offset: Offset(0, compact ? 12 : 18),
                    blurRadius: compact ? 20 : 28,
                  ),
                  const BoxShadow(
                    color: Color(0x80FFFFFF),
                    offset: Offset(0, -5),
                    blurRadius: 12,
                  ),
                ],
              ),
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                mainAxisSize: MainAxisSize.min,
                children: [
                  Text(
                    'Welcome back',
                    style: Theme.of(context).textTheme.headlineSmall?.copyWith(
                          color: const Color(0xFF24233A),
                          fontWeight: FontWeight.w700,
                        ),
                  ),
                  const SizedBox(height: 10),
                  const Text(
                    'Use soft volume for the object, but keep content and focus states crisp.',
                    style: TextStyle(color: Color(0xFF58556F)),
                  ),
                  const SizedBox(height: 18),
                  FilledButton(
                    onPressed: onPressed,
                    style: FilledButton.styleFrom(
                      minimumSize: const Size(48, 48),
                      padding: const EdgeInsets.symmetric(horizontal: 18, vertical: 10),
                      foregroundColor: const Color(0xFF24233A),
                      backgroundColor: Colors.white,
                      shape: RoundedRectangleBorder(
                        borderRadius: BorderRadius.circular(20),
                        side: const BorderSide(color: Color(0xFF554D86)),
                      ),
                    ),
                    child: const Text('Continue learning'),
                  ),
                ],
              ),
            ),
          ),
        );
      },
    );
  }
}
